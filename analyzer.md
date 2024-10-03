**Prompt [Try this prompt in Copilot for Microsoft 365](https://www.microsoft365.com/chat/entity1-d870f6cd-4aa5-4d42-9626-ab690c041429/eyJpZCI6IlZYTmxjbFl4ZkdoMGRIQnpPaTh2YzNWaWMzUnlZWFJsTFdsdWRDNXZabVpwWTJVdVkyOXRMM3hQU1VRNk9HVTNNV0kzTldVdE1tTTRPUzAwWVRVNExUbGpOemN0TWpaa016VXdOREkyTkRZeWZEaGhNemszTkRobUxUVTNZbVl0TkRRM05pMWlNall4TFRZMk5qRTVOemd4TURjM1lYd3lNREkwTFRFd0xUQXpWREUzT2pVeE9qTXhMalExTWpVMU9UZGEiLCJzY2VuYXJpbyI6InNoYXJlTGlua1ZpYVJpY2hDb3B5IiwicHJvcGVydGllcyI6eyJwcm9tcHRTb3VyY2UiOiJ1c2VyIiwiY2xpY2tUaW1lc3RhbXAiOiIyMDI0LTEwLTAzVDE3OjUxOjMwLjQ1NFoifSwidmVyc2lvbiI6MS4xfQ)**
Using python or AI, I want to mark the corners of a building and create an (x,y) coordinte of each corner or angle. The values should be in decimal notation
**Response**
To mark the corners of a building and create (x, y) coordinates for each corner using Python or AI, you can use computer vision libraries like OpenCV along with some AI models for object detection. Here’s a general approach you can follow:

1. **Install Required Libraries**: You will need OpenCV and NumPy for image processing and handling arrays. You can install them using pip:
    ```python
    pip install opencv-python numpy
    ```

2. **Load and Preprocess the Image**: Load the image of the building and preprocess it to enhance the edges and corners.
    ```python
    import cv2
    import numpy as np

    # Load the image
    image = cv2.imread('building.jpg')

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    ```

3. **Detect Edges and Corners**: Use edge detection and corner detection algorithms to find the corners of the building.
    ```python
    # Detect edges using Canny edge detector
    edges = cv2.Canny(blurred, 50, 150)

    # Detect corners using Harris Corner Detection
    corners = cv2.cornerHarris(edges, 2, 3, 0.04)

    # Dilate corner image to enhance corner points
    corners = cv2.dilate(corners, None)

    # Threshold for an optimal value, it may vary depending on the image.
    image[corners > 0.01 * corners.max()] = [0, 0, 255]
    ```

4. **Find Contours and Approximate Polygon**: Find contours and approximate the polygon to get the corner points.
    ```python
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours to find the polygon
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # If the approximated contour has 4 points, we assume it is a rectangle (building)
        if len(approx) == 4:
            for point in approx:
                x, y = point
                print(f"Corner: ({x}, {y})")
                cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
    ```

5. **Display the Result**: Display the image with marked corners.
    ```python
    # Display the image with corners marked
    cv2.imshow('Corners', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ```

This code will help you detect and mark the corners of a building in an image and print the (x, y) coordinates of each corner in decimal notation.

Would you like more details on any specific part of this process?