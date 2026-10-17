#include <iostream>
#include <iomanip>
#include "include/images/bitmap.h"

static void print_histogram(const char* name, const unsigned int* hist) {
    std::cout << name << "    ";
    for (unsigned int i = 0; i < 256; i++) {
        std::cout << std::setw(7) << hist[i];
    }
    std::cout << std::endl;
}

int main(const int argc, char** argv) {
    const char* path = argc > 1 ? argv[1] : "../lena.bmp";

    BMP_header headers(path);
    Bitmap image(headers, path);

    unsigned int last_x = headers.width - 1;
    unsigned int last_y = headers.height - 1;
    Pixel left_up = image.get_pixel(0, 0);
    Pixel right_up = image.get_pixel(last_x, 0);
    Pixel left_down = image.get_pixel(0, last_y);
    Pixel right_down = image.get_pixel(last_x, last_y);

    left_up.print_pixel(); std::cout << "   ";
    right_up.print_pixel(); std::cout << std::endl;
    left_down.print_pixel(); std::cout << "    ";
    right_down.print_pixel(); std::cout << std::endl;

    unsigned int hist_y[256]{};
    unsigned int hist_r[256]{};
    unsigned int hist_g[256]{};
    unsigned int hist_b[256]{};
    image.histogram(hist_y, &Pixel::Y);
    image.histogram(hist_r, &Pixel::R);
    image.histogram(hist_g, &Pixel::G);
    image.histogram(hist_b, &Pixel::B);

    std::cout << "value";
    for (unsigned int i = 0; i < 256; i++) {
        std::cout << std::setw(7) << i;
    }
    std::cout << std::endl;

    print_histogram("Y", hist_y);
    print_histogram("R", hist_r);
    print_histogram("G", hist_g);
    print_histogram("B", hist_b);
}
