<!-- -*- coding: utf-8-unix; mode: gfm -*- -->

# Photo credits

## Radio astronomy and orbital launch vehicle

All photos under the [Unsplash license](https://unsplash.com/license). Modification allowed. Attribution unnecessary but appreciated.

* [Very Large Array radio telescope at sunrise](https://unsplash.com/photos/Wj1D-qiOseE), Socorro, United States. Photo by [Donald Giannatti](https://unsplash.com/@wizwow) on [Unsplash](https://unsplash.com).

* [Falcon Heavy rocket taking off from Kennedy Space Center during daytime](https://unsplash.com/photos/OHOU-5UVIYQ), Merritt Island, United States. Photo by [SpaceX](https://unsplash.com/@spacex) on [Unsplash](https://unsplash.com).

* [Compact code sample with syntax highlighting](https://unsplash.com/photos/cvBBO4PzWPg). Photo by [Markus Spiske](https://unsplash.com/@markusspiske) on [Unsplash](https://unsplash.com). Modified as follow: fix white balance, posterize to 3 levels, increase contrast, convert background color to transparency, change transparency by adding a [layer mask](https://www.gimp.org/tutorials/Layer_Masks) and filling it up with a linear vertical black-to-white gradient.

## Subject symbols

Background photo under the [Unsplash license](https://unsplash.com/license). Modification allowed. Attribution unnecessary but appreciated.

* [Close-up view of a laptop's printed circuit board](https://unsplash.com/photos/FO7JIlwjOtU). Photo by [Alexandre Debiève](https://unsplash.com/@alexkixa) on [Unsplash](https://unsplash.com).

Icons under the [Flaticon Content license](https://www.freepikcompany.com/legal#nav-flaticon-agreement). Modification allowed. Attribution required.

* Lineal style icons, black and color: [books](https://www.flaticon.com/free-icon/books_3221555), [flask](https://www.flaticon.com/free-icon/flask_3034695), [rise](https://www.flaticon.com/free-icon/rising_1141881), [test tubes](https://www.flaticon.com/free-icon/test-tubes_3215503), [timing belt](https://www.flaticon.com/free-icon/timing-belt_2825598). Icons made by [Freepik](https://www.flaticon.com/authors/freepik) from [Flaticon](https://www.flaticon.com).

Strathclyde faculty colors taken from the [University's branding guidelines](https://www.strath.ac.uk/branding) and slightly lightened by adding +10 lightness in HSL color space.

|            | Business | Engineering | Humanities | Science |
| ---------- | -------- | ----------- | ---------- | ------- |
| Hue        |        1 |         200 |         19 |      86 |
| Saturation |       87 |         100 |         94 |      67 |
| Value      |       88 |          64 |         91 |      55 |
| Red        |      225 |           0 |        231 |     100 |
| Green      |       31 |         110 |         84 |     141 |
| Blue       |       29 |         163 |         14 |      47 |
| HTML       |   e11f1d |      006ea3 |     e7540e |  648d2f |

# More photos

Look for "code" or "programmer" on [Unsplash](https://unsplash.com), [Pexels](https://www.pexels.com), [StockSnap](https://stocksnap.io), [Pixabay](https://pixabay.com)... Always check the license.

# Export SVG to PNG with Inkscape

Use *File > Export PNG Image...* or the command line interface (`--export-area-page` is the default so it can be left out):

```shell
# Export to the original size by using the original resolution,
# typically 72 dpi for photographs
inkscape --export-png=out.png --export-area-page --export-dpi=72 in.svg

# Export to a smaller size by using --export-width or --export-height
inkscape --export-png=out.png --export-area-page --export-width=250 in.svg
```
