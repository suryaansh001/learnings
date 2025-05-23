#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;

int main() {
    // Load images
    Mat img1 = imread("image.png", IMREAD_GRAYSCALE);
    Mat img2 = imread("wolf.jpg", IMREAD_GRAYSCALE);

    // Initialize ORB detector
    Ptr<ORB> orb = ORB::create(500); // Max keypoints to be detected is 500

    // Detect keypoints and compute descriptors
    vector<KeyPoint> keypoints1, keypoints2;
    Mat descriptors1, descriptors2;
    orb->detectAndCompute(img1, noArray(), keypoints1, descriptors1);
    orb->detectAndCompute(img2, noArray(), keypoints2, descriptors2);

    // Match descriptors using Hamming distance (since ORB uses binary descriptors)
    BFMatcher matcher(NORM_HAMMING);
    vector<DMatch> matches;
    matcher.match(descriptors1, descriptors2, matches);

    // Filter good matches
    vector<DMatch> good_matches;
    for (const auto& match : matches) {
        if (match.distance < 0.7 * matches[0].distance) {
            good_matches.push_back(match);
        }
    }

    // Draw matches
    Mat img_matches;
    drawMatches(img1, keypoints1, img2, keypoints2, good_matches, img_matches);

    // Display result
    imshow("ORB Matches", img_matches);
    waitKey(0);
    return 0;
}