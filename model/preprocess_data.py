import os
import cv2
import json

os.mkdir("./data/custom/images/")
os.mkdir("./data/custom/labels")

with open("data/raw_data/annotations.json", "r") as rf:
    raw_data = json.loads(rf.read())
    images = raw_data["images"]
    annotations = raw_data["annotations"]

# Loop through each batch folder.
raw_data_content = os.listdir("./data/raw_data")
raw_data_content.remove("annotations.json")
for batch in raw_data_content:
    for file in os.listdir("./data/raw_data/" + batch):
        # Resize image.
        img = cv2.imread("./data/raw_data/" + batch + "/" + file)
        img = cv2.resize(img, (416, 416), interpolation = cv2.INTER_LINEAR)
        cv2.imwrite("./data/raw_data/" + batch + "/" + file, img)

        # Move image to ./data/custom/images/
        if file != "0.jpg":
            file = file.strip("0")

        os.rename("./data/raw_data/" + batch + "/" + file, "./data/custom/images/" + file)
        print("Moved " + "./data/raw_data/" + batch + "/" + file + " -->\n      ./data/custom/images/" + file)
    os.rmdir("./data/raw_data/" + batch)


info = {}
for i in range(len(annotations)):
    image_id = annotations[i]["image_id"]
    bbox = annotations[i]["bbox"]
    w = images[image_id]["width"]
    h = images[image_id]["height"]

    if info.get(image_id) == None:
        info[image_id] = []

    info[image_id].append("0 " + " ".join([str(i) for i in [
        bbox[0] / w, bbox[1] / h,
        bbox[2] / w, bbox[3] / h
    ]]))
    print("Labelled " + str(image_id) + ".jpg")


for key in info.keys():
    with open("./data/custom/labels/" + str(key) + ".txt", "w") as wf:
        for row in info[key]:
            wf.write(row + "\n")
    print("Created ./data/custom/labels/" + str(key) + ".txt")


with open("./data/custom/train.txt", "w") as wf:
    for file in range(int(1500*0.75)):
        wf.write("./data/custom/images/" + str(file) + ".jpg\n")

with open("./data/custom/valid.txt", "w") as wf:
    for file in range(int(1500*0.75), 1500):
        wf.write("./data/custom/images/" + str(file) + ".jpg\n")