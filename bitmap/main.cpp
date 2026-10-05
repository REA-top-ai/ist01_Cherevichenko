#include <iostream>
#include <fstream>

#define ERR_IF_FALSE(check, err_message, arg) if (!(check)) {std::cerr << err_message << arg << std::endl; return 1;}
constexpr auto ERR_CANT_OPEN_FILE{"File can't be open: "};
constexpr auto ERR_IS_NOT_BMP{"File is not BMP: "};
constexpr auto ERR_UNSUPPORTED_BIT_COUNT{"Unsupported bits per pixel: "};
constexpr auto ERR_CANT_READ_IMAGE{"Can't read image data: "};

#pragma pack(push, 1)
struct BMP_header {
    char sign[2];
    unsigned int file_size;
    unsigned int reserved;
    unsigned int data_offset;
    unsigned int data_size;
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

static Pixel get_pixel(const Pixel* pixels, unsigned int x, unsigned int y, unsigned int width, unsigned int height) {
    unsigned int row = height - 1 - y;
    return pixels[row * width + x];
}

static void print_pixel(const Pixel pixel) {
    std::cout << "R: " << static_cast<int>(pixel.R) << " G: " << static_cast<int>(pixel.G) << " B: " << static_cast<int>(pixel.B);
}

int main(const int argc, char** argv) {
    unsigned char headers[54]{};
    const char* path = argc > 1 ? argv[1] : "../lena.bmp";

    bool file_was_read = load_file_bytes(path, headers, 54);
    ERR_IF_FALSE(file_was_read, ERR_CANT_OPEN_FILE, path);
    ERR_IF_FALSE(is_BMP(headers), ERR_IS_NOT_BMP, path);

    auto* headers_values = reinterpret_cast<BMP_header*>(headers);

    /*
    auto [sign, file_size, reserved,
        data_offset, data_size, width, height, planes, bit_count,
        compression, image_size, x_pixels_per_m, y_pixels_per_m,
        colors_used, color_important] = *headers_values;
    */

    auto width = headers_values->width;
    auto height = headers_values->height;
    auto bit_count = headers_values->bit_count;
    auto image_size = headers_values->image_size;
    auto data_offset = headers_values->data_offset;

    ERR_IF_FALSE(bit_count == 24, ERR_UNSUPPORTED_BIT_COUNT, bit_count);

    auto* pixels = new Pixel[image_size / sizeof(Pixel)];
    bool image_was_read = load_file_bytes(path, reinterpret_cast<unsigned char*>(pixels), image_size, data_offset);
    if (!image_was_read) {delete[] pixels;}
    ERR_IF_FALSE(image_was_read, ERR_CANT_READ_IMAGE, path);

    unsigned int last_x = width - 1;
    unsigned int last_y = height - 1;

    Pixel left_up = get_pixel(pixels, 0, 0, width, height);
    Pixel right_up = get_pixel(pixels, last_x, 0, width, height);
    Pixel left_down = get_pixel(pixels, 0, last_y, width, height);
    Pixel right_down = get_pixel(pixels, last_x, last_y, width, height);

    print_pixel(left_up); std::cout << "   ";
    print_pixel(right_up); std::cout << std::endl;
    print_pixel(left_down); std::cout << "    ";
    print_pixel(right_down); std::cout << std::endl;

    delete[] pixels;
    return 0;
}