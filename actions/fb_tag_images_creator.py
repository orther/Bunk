from os   import mkdir
from time import time

import Image
import ImageFont
import ImageChops
import ImageDraw
import ImageEnhance

from bunk.action import BunkAction

from bunk.response_formatters.json_formatter  import JsonFormatter

# ------------------------------------------------------------------------------------------------------------------
# BANNER SETTINGS
# ------------------------------------------------------------------------------------------------------------------

banner_color      = "#ffffff"
banner_num_pieces = 5
banner_size       = (485, 68)
font_file         = "/home/brandon/projects/Bunk/VERDANA.TTF"
font_color        = "#ff0000"
storage_path      = "/var/www/think-done/www/files/fb_images"
storage_web_path  = "/files/fb_images"

# ------------------------------------------------------------------------------------------------------------------
# RESPON ERROR CODES
# ------------------------------------------------------------------------------------------------------------------

RESP_ERROR_CODE_NO_BANNER_TEXT_RECEIVED = 1

# ------------------------------------------------------------------------------------------------------------------
# ACTION CLASS
# ------------------------------------------------------------------------------------------------------------------

class FbTagImageCreatorAction (BunkAction):

    # ------------------------------------------------------------------------------------------------------------------
    # INTERNAL METHODS
    # ------------------------------------------------------------------------------------------------------------------

    def _setup (self):
        """
        Set response formatter.
        """

        self._response_formatter = JsonFormatter

    # ------------------------------------------------------------------------------------------------------------------

    def _create_banner_pieces (self, banner_text, storage_path, file_prefix=None):
        """
        Create banner pieces images, store them to disk and return a tuple of files created.

        @param banner_text  (str)
        @param storage_path (str)
        @param file_prefix  (str)

        @return (tuple)
        """

        # create image
        banner = Image.new("RGB", banner_size, banner_color)

        # load font and calculate font size needed to fit all text
        font_size    = 20
        font         = ImageFont.truetype(font_file, font_size)
        text_size    = font.getsize(banner_text)
        resize_ratio = min(float(banner_size[0])/text_size[0], float(banner_size[1])/text_size[1])

        # load font with new size and calculate offsets to center text
        font         = ImageFont.truetype(font_file, int(font_size * resize_ratio))
        text_size    = font.getsize(banner_text)
        text_padding = ((banner_size[0] - text_size[0]) / 2,
                        (banner_size[1] - text_size[1]) / 2)

        # draw text to banner
        draw = ImageDraw.Draw(banner)

        draw.text(text_padding, banner_text, font = font, fill = font_color)

        # chop image into 5 pieces
        chop_width = banner_size[0] / banner_num_pieces
        chop_box   = (0, 0, chop_width, banner_size[1])

        banner_piece_files = list()

        for i in xrange(banner_num_pieces):
            piece_cords  = (i * chop_width, 0, chop_width * (i + 1), banner_size[1])
            banner_piece = banner.crop(piece_cords)
            file_name    = "%s%s.png" % (file_prefix, banner_num_pieces - i)

            # write banner piece image to disk
            banner_piece.save("%s/%s" % (storage_path, file_name), "PNG")

            banner_piece_files.append(file_name)

        return tuple(banner_piece_files)

    # ------------------------------------------------------------------------------------------------------------------
    # REQUEST HANDLERS
    # ------------------------------------------------------------------------------------------------------------------

    def bunk_post (self):

        # NOTE: I should use an Elements model here

        # set and validate image text
        if not "banner_text" in self._client.params:
            self.respond_error(RESP_ERROR_CODE_NO_BANNER_TEXT_RECEIVED, "No banner text received")
            return

        # build storage path
        unique_dir_name     = "%s" % float(time())
        unique_storage_path = "%s/%s" % (storage_path, unique_dir_name)

        print "TEST>>>>>"
        mkdir(unique_storage_path)

        # create images
        pieces = self._create_banner_pieces(self._client.params["banner_text"], unique_storage_path,
                                            file_prefix="fb_image_")

        response = {
            "path":   "%s/%s" % (storage_web_path, unique_dir_name),
            "pieces": pieces
        }

        # respond with image details
        self.respond(response)
