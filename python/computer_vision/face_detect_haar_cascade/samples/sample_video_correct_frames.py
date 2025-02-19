# FACE DETECTION ON RECORDED VIDEO TO CHECK TOTAL FRAMES WITH DETECTED FACE

# Built-int imports
import os

# My own imports
import face_detect_hc as fdhc
import get_assets_folder as gaf

# General module imports
import cv2 as cv
import time


class CorrectFramesCounter:
    def __init__(self, CAP, OUT):
        self.total_frames = 0
        self.correct_frames = 0
        self.CAP = CAP
        self.OUT = OUT

    def main(self):
        # check_results if video loaded correctly
        if (self.CAP.isOpened() == False):
            print("Error opening video stream or file")
            return False
        else:
            while (self.CAP.isOpened()):
                # Get specific read image from each instant from CAP capture
                ret, image = CAP.read()

                if ret == True:
                    # Apply face_detect algorithm to each image capture
                    fd = fdhc.FaceDetector(
                        image, show_results=True, only_biggest_face=True)
                    faces = fd.face_detect()

                    # Write video results in new video
                    self.OUT.write(image)

                    # Count correct frames for face_detect
                    if (len(faces) > 0):
                        self.correct_frames = self.correct_frames + 1
                    self.total_frames = self.total_frames + 1

                    # Exit when "q" is pressed
                    if (cv.waitKey(1) & 0xFF == ord("q")):
                        return True

                else:
                    return True

        # When CAP is finished processing, close the capture object
        self.CAP.release()
        self.OUT.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    # Get assets folder in repo for the samples
    ASSETS_FOLDER = gaf.get_assets_folder_path()

    CAP = cv.VideoCapture(os.path.join(
        ASSETS_FOLDER, "videos", "sample_video_1.mp4"))

    fourcc = cv.VideoWriter_fourcc(*'MJPG')
    OUT = cv.VideoWriter("sample_video_1_output.avi", fourcc,
                         20.0, (int(CAP.get(3)), int(CAP.get(4))))

    start_time = time.time()

    # Run main frame analyzer
    check_results = CorrectFramesCounter(CAP, OUT)
    if (check_results.main() == True):
        # Gather frame analyzer results
        total = check_results.total_frames
        correct = check_results.correct_frames
        success = str((float(correct) / float(total)) * 100)

        print("\n\n----------- RESULTS -----------")
        print(" --> Total Frames: {}".format(total))
        print(" --> Correct Frames: {}".format(correct))
        print(" --> Succes Rate: {0} %".format(success))
        print(" ---- %s seconds ----" % (time.time() - start_time))
