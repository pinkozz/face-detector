# face-detector
OpenCV face detection software that detects faces by identifying facial features in a photo or video using machine learning algorithms. It first looks for an eye, and from there it identifies other facial features. It then compares these features to training data to confirm it has detected a face.

# Table of contents
• [Features](https://github.com/pinkozz/face-detector#features)

• [Installation](https://github.com/pinkozz/face-detector#installation)

• [Usage](https://github.com/pinkozz/face-detector#usage)

• [Contributing](https://github.com/pinkozz/face-detector#contributing)

• [License](https://github.com/pinkozz/face-detector#license)
# Features
• Detect face using your own images!

• Easy-to-use and extandable codebase

# Installation
1. Clone this repository to your local machine using this command:
   
   ```shell
   git clone https://github.com/pinkozz/face-detector
   ```
2. Navigate to project folder:
   
   ```shell
   cd face-detector
   ```
3. Once you have installed the face detector open <b>face_detection.py</b> and change "../face/test.jpg" to your actual path to test.jpg:
   
   ```shell
   img = cv.imread('../face/test.jpg')
   ```

4. Change "../detection-model/haar_face.xml" to your actual path to haar_face.xml:

   ```shell
   haar_cascade = cv.CascadeClassifier('../detection-model/haar_face.xml')
   ```

5. You can add your own photo to test the detector:

   1)Go to <b>../face</b> and add your own photo there
   
   2)Change path to foto from <b>PATH_TO_YOUR_PHOTO</b> to your actual path to the photo:

      ```shell
       img = cv.imread('PATH_TO_YOUR_PHOTO')
      ```
6. Once all changes are done navigate to <b>"main"</b> folder in the project folder and run the program

  ```shell
   python3 face_detection.py
  ```

<b>!!NOTE!! The face detector is built for detecting one face per image. If you added an image with 2 or more faces in it, the program might not work properly. To change that go to ../main/face_detection.py and pass smaller value to minNeighbors. The less the value is, the more faces will be detected.</b>

```shell
  faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
```

# Usage
Once the program up and running it will detect and point on the faces on the photo.

# Contributing
Contributions to the face-detector are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes and commit them with descriptive commit messages.
5. Push your changes to your forked repository.
6. Submit a pull request to the main repository.

Please ensure that your contributions align with the project's coding style, guidelines, and licensing.

# License
The face-detector is open-source software released under the MIT License.

Feel free to customize this guide page based on your specific bot implementation and project requirements.
