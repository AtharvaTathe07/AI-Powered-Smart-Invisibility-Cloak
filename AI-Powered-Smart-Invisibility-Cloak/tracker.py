"""
Object Tracking Module
AI-Powered Smart Invisibility Cloak
"""

import cv2

class CloakTracker:

    def __init__(self):
        self.previous_center = None

    def get_largest_contour(self, mask):

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        if len(contours) == 0:
            return None

        return max(contours, key=cv2.contourArea)

    def track(self, mask):

        contour = self.get_largest_contour(mask)

        if contour is None:
            return None

        x, y, w, h = cv2.boundingRect(contour)

        center = (
            x + w // 2,
            y + h // 2
        )

        self.previous_center = center

        return {
            "x": x,
            "y": y,
            "width": w,
            "height": h,
            "center": center
        }

if __name__ == "__main__":
    print("Tracker Module Loaded")
