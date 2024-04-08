### In this section, we learned how to create a fastapi that performs post, put, get, and delete operations on the SQLite database. The redoc output is as follows.

![screencapture-127-0-0-1-8000-redoc-2024-04-06-13_44_36](https://github.com/mori-cyber/PyDeploy/assets/65276280/6269167c-7c93-4c21-aac3-b5d1bf698f21)

### In the next part, a fast API is designed, which first adds an image to the database, then the desired image is read and the gender of the image is determined using the deep model that was the most popular on the gender-recognition-200k-images-celeba dataset. The opinion is evaluated that if the desired image is of a man, the number zero will be returned as a result, and if it is a woman, the number 1 will be returned. To apply the code, the version of TensorFlow must be installed according to the version of Python itself. Also, in order not to encounter the thread error, we must first install the thread, the method of installation of which is mentioned in the requirement.txt file.
### For install requirement packages please run this command in the terminal:
☺️ pip install -r requirement
### For run API code please run this command in the terminal:
☺️ uvicorn main:app --reload

☺️ Also at the end of each function: Thread(target=function_name).start() be inserted.

👀 The redoc output is:
![screencapture-127-0-0-1-8000-redoc-2024-04-06-23_23_39](https://github.com/mori-cyber/PyDeploy/assets/65276280/96ced81d-c8f7-40c7-8527-b422169a4fab)

