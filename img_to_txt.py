import cv2
import pytesseract


def parse_text(text):

    split_text = text.split()

    drug_name_index = split_text.index('for:')
    drug_name = split_text[drug_name_index + 1]

    frequency_index = split_text.index('Take')
    frequency = split_text[frequency_index + 1]

    amount_index = split_text.index('of')
    amount = split_text[amount_index + 1]

    return {
        "drug_name": drug_name,
        "frequency": frequency,
        "amount": amount
    }


def gen_txt():
    pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

    img = cv2.imread("uploads/sample.jpg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh1 = cv2.threshold(
        gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10000, 10000))

    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)

    im2 = img.copy()

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cropped = im2[y:y + h, x:x + w]

        text = pytesseract.image_to_string(cropped)

        return parse_text(text)
