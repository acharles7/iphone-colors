# Author: Charles Patel (charlespatel007@apkudo.com)

from typing import Literal

ColorName = Literal[
    "Green",
    "Yellow",
    "Alpine Green",
    "Midnight Green",
    "Blue",
    "Sierra Blue",
    "Pacific Blue",
    "Space Gray",
    "Graphite",
    "Silver",
    "Gold",
    "Rose Gold",
    "Black",
    "Jet Black",
    "Midnight",
    "Pink",
    "Coral",
    "Red",
    "White",
    "Starlight",
    "Purple",
    "Deep Purple",
    "Space Black",
    "Black Titanium",
    "Blue Titanium",
    "Natural Titanium",
    "White Titanium",
]

# https://support.apple.com/en-us/HT201296

IPHONE_COLORS: dict[str, set[ColorName]] = {
    "iPhone 3G": {"Black"},
    # https://support.apple.com/kb/SP565?locale=en_US
    "iPhone 3GS": {"Black"},
    # https://support.apple.com/kb/sp587?locale=en_US
    "iPhone 4": {"Black", "White"},
    # https://support.apple.com/kb/sp643?locale=en_US
    "iPhone 4s": {"Black", "White"},
    # https://support.apple.com/kb/sp655?locale=en_US
    "iPhone 5": {"Black", "Silver"},  # Black and Slate,  White and Silver
    # https://support.apple.com/kb/sp684?locale=en_US
    "iPhone 5c": {"White", "Pink", "Yellow", "Blue", "Green"},
    # https://support.apple.com/kb/sp685?locale=en_US
    "iPhone 5s": {"Space Gray", "Gold", "Silver"},
    # https://support.apple.com/kb/sp705?locale=en_US
    "iPhone 6": {"Silver", "Gold", "Space Gray"},
    # https://support.apple.com/kb/sp706?locale=en_US
    "iPhone 6 Plus": {"Silver", "Gold", "Space Gray"},
    # https://support.apple.com/kb/sp726?locale=en_US
    "iPhone 6s": {"Rose Gold", "Gold", "Silver", "Space Gray"},
    # https://support.apple.com/kb/sp727?locale=en_US
    "iPhone 6s Plus": {"Rose Gold", "Gold", "Silver", "Space Gray"},
    #  https://support.apple.com/kb/SP743?locale=en_US
    "iPhone 7": {"Rose Gold", "Gold", "Silver", "Black", "Jet Black", "Red"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/SP744?locale=en_US
    "iPhone 7 Plus": {"Rose Gold", "Gold", "Silver", "Black", "Jet Black", "Red"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/sp767?locale=en_US
    "iPhone 8": {"Gold", "Silver", "Space Gray", "Red"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/sp768?locale=en_US
    "iPhone 8 Plus": {"Gold", "Silver", "Space Gray", "Red"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/SP738?locale=en_US
    "iPhone SE": {"Silver", "Gold", "Space Gray", "Rose Gold"},  # (1st Gen)
    # https://support.apple.com/kb/sp770?locale=en_US
    "iPhone X": {"Space Gray", "Silver"},
    # https://support.apple.com/kb/SP781?locale=en_US
    "iPhone XR": {"Red", "Yellow", "White", "Coral", "Black", "Blue"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/SP779?locale=en_US
    "iPhone XS": {"Gold", "Space Gray", "Silver"},
    # https://support.apple.com/kb/SP780?locale=en_US
    "iPhone XS Max": {"Gold", "Space Gray", "Silver"},
    # https://support.apple.com/kb/SP804?locale=en_US
    "iPhone 11": {"Black", "Green", "Yellow", "Purple", "Red", "White"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/SP805?locale=en_US
    "iPhone 11 Pro": {"Gold", "Space Gray", "Silver", "Midnight Green"},
    # https://support.apple.com/kb/SP806?locale=en_US
    "iPhone 11 Pro Max": {"Gold", "Space Gray", "Silver", "Midnight Green"},
    # https://support.apple.com/kb/SP820?locale=en_US
    "iPhone SE (2nd Gen)": {"Black", "White", "Red"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/SP830?locale=en_US
    "iPhone 12": {"Black", "White", "Red", "Green", "Blue", "Purple"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/SP829?locale=en_US
    "iPhone 12 Mini": {"Black", "White", "Red", "Green", "Blue", "Purple"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/SP831?locale=en_US
    "iPhone 12 Pro": {"Silver", "Graphite", "Gold", "Pacific Blue"},
    # https://support.apple.com/kb/SP832?locale=en_US
    "iPhone 12 Pro Max": {"Silver", "Graphite", "Gold", "Pacific Blue"},
    # https://support.apple.com/kb/SP851?locale=en_US
    "iPhone 13": {"Red", "Starlight", "Midnight", "Blue", "Pink", "Green"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/SP851?locale=en_US
    "iPhone 13 Mini": {"Red", "Starlight", "Midnight", "Blue", "Pink", "Green"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/SP852?locale=en_US
    "iPhone 13 Pro": {"Graphite", "Gold", "Silver", "Sierra Blue", "Alpine Green"},
    # https://support.apple.com/kb/SP852?locale=en_US
    "iPhone 13 Pro Max": {"Graphite", "Gold", "Silver", "Sierra Blue", "Alpine Green"},
    # https://support.apple.com/kb/SP820?locale=en_US
    "iPhone SE (3rd Gen)": {"Red", "Starlight", "Midnight"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/SP873?locale=en_US
    "iPhone 14": {"Midnight", "Purple", "Starlight", "Red", "Blue", "Yellow"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/SP874?locale=en_US
    "iPhone 14 Plus": {"Midnight", "Purple", "Starlight", "Red", "Blue", "Yellow"},  # (PRODUCT)RED™
    # https://support.apple.com/kb/SP875?locale=en_US
    "iPhone 14 Pro": {"Space Black", "Silver", "Gold", "Deep Purple"},
    # https://support.apple.com/kb/SP876?locale=en_US
    "iPhone 14 Pro Max": {"Space Black", "Silver", "Gold", "Deep Purple"},
    # https://support.apple.com/kb/SP901?locale=en_US
    "iPhone 15": {"Black", "Blue", "Green", "Yellow", "Pink"},
    # https://support.apple.com/kb/SP901?locale=en_US
    "iPhone 15 Plus": {"Black", "Blue", "Green", "Yellow", "Pink"},
    # https://support.apple.com/kb/SP903?locale=en_US
    "iPhone 15 Pro": {"Black Titanium", "White Titanium", "Blue Titanium", "Natural Titanium"},
    # https://support.apple.com/kb/SP904?locale=en_US
    "iPhone 15 Pro Max": {"Black Titanium", "White Titanium", "Blue Titanium", "Natural Titanium"},
}
