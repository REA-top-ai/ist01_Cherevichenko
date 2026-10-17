#include "../../include/images/bitmap.h"
#include "../../include/file_loader.h"
#include "../../include/errors.h"

#include <cmath>
#include <stdexcept>

Bitmap::Bitmap(BMP_header headers, const char* path) : headers{headers} {
    if (!headers.is_supported_bit_count()) {throw std::runtime_error(ERR_UNSUPPORTED_BIT_COUNT);}
    if (!headers.is_supported_compression()) {throw std::runtime_error(ERR_UNSUPPORTED_COMPRESSION);}

    this->pixels = new unsigned char[headers.image_size];
    bool loaded = load(path);
    if (!loaded) {delete[] pixels; throw std::runtime_error(ERR_CANT_READ_IMAGE);}
}

bool Bitmap::load(const char* path) {
    return load_file_bytes(path, pixels, headers.image_size, headers.data_offset);
}

Pixel Bitmap::get_pixel(unsigned int x, unsigned int y) const {
    return to_pixel(get_pixel_address(x, y));
}

void Bitmap::histogram(unsigned int* hist, unsigned char Pixel::* channel) const {
    unsigned int x; unsigned int y;
    for (x = 0; x < headers.width; x++) {
        for (y = 0; y < headers.height; y++) {
            Pixel pixel = get_pixel(x, y);
            hist[pixel.*channel] ++;
        }
    }
}

Bitmap::~Bitmap() {
    delete[] pixels;
}

const unsigned char* Bitmap::get_pixel_address(unsigned int x, unsigned int y) const {
    unsigned int row = headers.height - 1 - y;
    return pixels + (row * headers.width + x) * (headers.bit_count / 8);
}

Pixel Bitmap::to_pixel(const unsigned char* pixel) const {
    if (headers.bit_count == 16) {
        return pixel_from_16bit(pixel);
    }

    return Pixel{pixel[0], pixel[1], pixel[2]};
}

unsigned char Bitmap::recover_16b_value (unsigned char subpixel, pixel_color color) {
    switch (color) {
        case r:
            return subpixel * (pow(2, 8) - 1) / (pow(2, 5) - 1);
            break;
        case g:
            return subpixel * (pow(2, 8) - 1) / (pow(2, 6) - 1);
            break;
        case b:
            return subpixel * (pow(2, 8) - 1) / (pow(2, 5) - 1);
            break;
    }

        return 0;
}

Pixel Bitmap::pixel_from_16bit(const unsigned char* pixel) {
    const unsigned short value = *reinterpret_cast<const unsigned short*>(pixel);

    constexpr unsigned short b_16bit_mask = 0B0000000000011111;
    constexpr unsigned short g_16bit_mask = 0B0000011111100000;
    constexpr unsigned short r_16bit_mask = 0B1111100000000000;

    const unsigned char R = recover_16b_value((value & r_16bit_mask) >> 11, r);
    const unsigned char G = recover_16b_value((value & g_16bit_mask) >> 5, g);
    const unsigned char B = recover_16b_value(value & b_16bit_mask, b);

    return Pixel{B, G, R};
}
