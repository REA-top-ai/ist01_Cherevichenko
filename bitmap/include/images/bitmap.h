#pragma once

#include "pixel.h"
#include "bmp_header.h"

class Bitmap {
    public:
        Bitmap(BMP_header headers, const char* path);
        bool load(const char* path);
        Pixel get_pixel(unsigned int x, unsigned int y) const;
        void histogram(unsigned int* hist, unsigned char Pixel::* channel) const;
        ~Bitmap();

    private:
        BMP_header headers;
        unsigned char* pixels;

        const unsigned char* get_pixel_address(unsigned int x, unsigned int y) const;
        Pixel to_pixel(const unsigned char* pixel) const;

        enum pixel_color{r, g, b};
        static unsigned char recover_16b_value (unsigned char subpixel, pixel_color color);
        static Pixel pixel_from_16bit(const unsigned char* pixel);
};
