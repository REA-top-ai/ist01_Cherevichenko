#include <iostream>
#include <fstream>

#define ERR_IF_FALSE(check, err_message, arg) if (!(check)) {std::cerr << err_message << arg << std::endl; return 1;}
constexpr auto ERR_CANT_OPEN_FILE{"File can't be open: "};
constexpr auto ERR_IS_NOT_BMP{"File is not BMP: "};
constexpr auto ERR_UNSUPPORTED_BIT_COUNT{"Unsupported bits per pixel: "};
constexpr auto ERR_CANT_READ_IMAGE{"Can't read image data: "};
constexpr auto ERR_UNSUPPORTED_COMPRESSION{"Unsupported compression: "};

#pragma pack(push, 1)
struct BMP_header {
    char sign[2];
    unsigned int file_size;
    unsigned int reserved;
    unsigned int data_offset;
    unsigned int info_header_size;
    unsigned int width;
    unsigned int height;
    unsigned short planes;
    unsigned short bit_count;
    unsigned int compression;
    unsigned int image_size;
    unsigned int x_pixels_per_m;
    unsigned int y_pixels_per_m;
    unsigned int colors_used;
    unsigned int color_important;
};
#pragma pack(pop)

#pragma pack(push, 1)
struct Pixel {
    unsigned char B;
    unsigned char G;
    unsigned char R;
};
#pragma pack(pop)

static bool load_file_bytes(const char* path, unsigned char* buffer, const unsigned int size, const unsigned int offset = 0) {
    std::ifstream file(path, std::ios::binary);
    if (!file) { return false; }
    file.seekg(offset);
    file.read(reinterpret_cast<char*>(buffer), size);
    return true;
}

static bool is_BMP(const unsigned char* headers) {
    return (headers[0] == 'B' && headers[1] == 'M');
}

static const unsigned char* get_pixel_address(const unsigned char* pixels, unsigned int x, unsigned int y, unsigned int width, unsigned int height, unsigned int bytes_per_pixel) {
    unsigned int row = height - 1 - y;
    return pixels + (row * width + x) * bytes_per_pixel;
}

static void print_pixel(const Pixel pixel) {
    std::cout << "R: " << static_cast<int>(pixel.R) << " G: " << static_cast<int>(pixel.G) << " B: " << static_cast<int>(pixel.B);
}

static unsigned int find_shift(unsigned int mask) {
    unsigned int shift = 0;
    while ((mask & 1) == 0) {
        mask >>= 1; shift++;
    }

    return shift;
}

static unsigned char get_channel(unsigned short value, unsigned int mask) {
    unsigned int shift = find_shift(mask);
    return static_cast<unsigned char>(((value & mask) >> shift) * 255 / (mask >> shift));
}

static Pixel pixel_from_16bit(const unsigned char* pixel, unsigned int mask_red, unsigned int mask_green, unsigned int mask_blue) {
    const unsigned short value = *reinterpret_cast<const unsigned short*>(pixel);

    const unsigned char R = get_channel(value, mask_red);
    const unsigned char G = get_channel(value, mask_green);
    const unsigned char B = get_channel(value, mask_blue);

    return Pixel{B, G, R};
}

static Pixel to_pixel(const unsigned char* pixel, unsigned int bit_count, unsigned int mask_red, unsigned int mask_green, unsigned int mask_blue) {
    if (bit_count == 16) {
        return pixel_from_16bit(pixel, mask_red, mask_green, mask_blue);
    }

    return *reinterpret_cast<const Pixel*>(pixel);
}

int main(const int argc, char** argv) {
    unsigned char headers[54]{};
    const char* path = argc > 1 ? argv[1] : "../lena.bmp";

    bool file_was_read = load_file_bytes(path, headers, 54);
    ERR_IF_FALSE(file_was_read, ERR_CANT_OPEN_FILE, path);
    ERR_IF_FALSE(is_BMP(headers), ERR_IS_NOT_BMP, path);

    auto* headers_values = reinterpret_cast<BMP_header*>(headers);

    auto [sign, file_size, reserved,
        data_offset, info_header_size, width, height, planes, bit_count,
        compression, image_size, x_pixels_per_m, y_pixels_per_m,
        colors_used, color_important] = *headers_values;

    ERR_IF_FALSE(bit_count == 24 || bit_count == 16, ERR_UNSUPPORTED_BIT_COUNT, bit_count);

    unsigned int mask_red = 0x7C00;
    unsigned int mask_green = 0x03E0;
    unsigned int mask_blue = 0x001F;
    if (bit_count == 16) {
        ERR_IF_FALSE(compression == 0 || compression == 3, ERR_UNSUPPORTED_COMPRESSION, compression);

        if (compression == 3) {
            load_file_bytes(path, reinterpret_cast<unsigned char*>(&mask_red), 4, 54);
            load_file_bytes(path, reinterpret_cast<unsigned char*>(&mask_green), 4, 58);
            load_file_bytes(path, reinterpret_cast<unsigned char*>(&mask_blue), 4, 62);
        }
    }

    auto pixels = new unsigned char[image_size];
    bool image_was_read = load_file_bytes(path, pixels, image_size, data_offset);
    if (!image_was_read) {delete[] pixels;}
    ERR_IF_FALSE(image_was_read, ERR_CANT_READ_IMAGE, path);

    unsigned int bytes_per_pixel = bit_count / 8;

    unsigned int last_x = width - 1;
    unsigned int last_y = height - 1;

    Pixel left_up = to_pixel(get_pixel_address(pixels, 0, 0, width, height, bytes_per_pixel), bit_count, mask_red, mask_green, mask_blue);
    Pixel right_up = to_pixel(get_pixel_address(pixels, last_x, 0, width, height, bytes_per_pixel), bit_count, mask_red, mask_green, mask_blue);
    Pixel left_down = to_pixel(get_pixel_address(pixels, 0, last_y, width, height, bytes_per_pixel), bit_count, mask_red, mask_green, mask_blue);
    Pixel right_down = to_pixel(get_pixel_address(pixels, last_x, last_y, width, height, bytes_per_pixel), bit_count, mask_red, mask_green, mask_blue);

    print_pixel(left_up); std::cout << "   ";
    print_pixel(right_up); std::cout << std::endl;
    print_pixel(left_down); std::cout << "    ";
    print_pixel(right_down); std::cout << std::endl;

    delete[] pixels;
    return 0;
}