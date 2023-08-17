from jetson_inference import imageNet
from jetson_utils import videoSource, videoOutput, cudaFont, Log


net = imageNet(model="resnet/resnet18onFire.onnx", labels="resnet/labels.txt", 
                 input_blob="input_0", output_blob="output_0")

camera = videoSource("/dev/video0", argv=["--input-width=720", "--input-height=720"]) # Change this to desired image input 
display = videoOutput("webrtc://@:8554/my_output")  # Replace with your WebRTC URL

font = cudaFont()

labelText = ""

alert = False

while True:

    img = camera.Capture()

    if img is None: # timeout
        continue  

    img_width = img.shape[1]
    img_height = img.shape[0]

    class_idx, confidence = net.Classify(img)
    class_desc = net.GetClassDesc(class_idx)

    predictions = net.Classify(img)

    classLabel = net.GetClassLabel(class_idx)
    confidence *= 100.0

    if "0" in classLabel:
        labelText = "Not On Fire"
    else:
        labelText = "On Fire"
        if not alert:
            print("Alert!!\nCheck the stream at http://ubuntu:8554/")
            # Include code here if you want to have an alert
            alert = True

    result_text = "Recognized: {} (Class #{}) {:.2f}%".format(class_desc, class_idx, confidence * 100, labelText)

    font.OverlayText(img, text=f"{confidence:05.2f}% {labelText}", 
                         x=5, y=5 + (font.GetSize() + 5),
                         color=font.White, background=font.Gray40)

    display.Render(img)
    display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))