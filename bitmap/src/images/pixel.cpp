#include "../../include/images/pixel.h"

#include <iostream>
#include <cmath>

Pixel::Pixel(unsigned char b, unsigned char g, unsigned char r) {
    B = b;
    G = g;
    R = r;
    Y = std::round(0.2126 * R + 0.7152 * G + 0.0722 * B);
}

void Pixel::print_pixel() const {
    std::cout << "R: " << static_cast<int>(R) << " G: " << static_cast<int>(G);
    std::cout << " B: " << static_cast<int>(B) << " Y: " << static_cast<int>(Y);

}
