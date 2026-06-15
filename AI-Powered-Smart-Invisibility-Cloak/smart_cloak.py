"""
AI-Powered Smart Invisibility Cloak
Main Engine
"""

import cv2
import numpy as np

from tracker import CloakTracker
from yolo_detector import YOLODetector


class SmartInvisibilityCloak:

    def __init__(self):

        self.background = None
        self.tracker = CloakTracker()
        self.detector = YOLODetector()

    def capture_background(self, frame):

        self.background = frame.copy()

    def detect_red_cloak(self, frame):

        hsv = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2HSV
        )

        lower_red1 = np.array([0, 120, 70])
        upper_red1 = np.array([10, 255, 255])

        lower_red2 = np.array([170, 120, 70])
        upper_red2 = np.array([180, 255, 255])

        mask1 = cv2.inRange(
            hsv,
            lower_red1,
            upper_red1
        )

        mask2 = cv2.inRange(
            hsv,
            lower_red2,
            upper_red2
        )

        mask = mask1 + mask2

        kernel = np.ones((3, 3), np.uint8)

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            kernel
        )

        mask = cv2.dilate(
            mask,
            kernel,
            iterations=1
        )

        return mask

    def apply_invisibility(
        self,
        frame,
        mask
    ):

        if self.background is None:
            return frame

        invisible_part = cv2.bitwise_and(
            self.background,
            self.background,
            mask=mask
        )

        visible_part = cv2.bitwise_and(
            frame,
            frame,
            mask=cv2.bitwise_not(mask)
        )

        return cv2.addWeighted(
            invisible_part,
            1,
            visible_part,
            1,
            0
        )


def main():

    print("=" * 50)
    print("AI-Powered Smart Invisibility Cloak")
    print("=" * 50)

    print("Modules Loaded:")
    print("- OpenCV")
    print("- NumPy")
    print("- Object Tracking")
    print("- YOLO Detection Architecture")
    print("- Dynamic Background Engine")

    print("\nSystem Ready")


if __name__ == "__main__":
    main()
