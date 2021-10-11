import os
import sys
import json
import pydicom
from pydicom.uid import generate_uid
from pathlib import Path
from scipy.ndimage.filters import gaussian_filter


def process_image(file, in_folder, out_folder, series_uid, settings):
    dcm_file_in = Path(in_folder) / file
    out_filename = series_uid + "#" + file.split("#", 1)[1]
    dcm_file_out = Path(out_folder) / out_filename    

    ds = pydicom.dcmread(dcm_file_in)
    ds.SeriesInstanceUID = series_uid
    ds.SOPInstanceUID = generate_uid()
    ds.SeriesNumber = ds.SeriesNumber + settings["series_offset"]
    ds.SeriesDescription = "FILTER(" + ds.SeriesDescription + ")"
    pixels = ds.pixel_array
    blurred_pixels = gaussian_filter(pixels, sigma=settings["sigma"])
    ds.PixelData = blurred_pixels.tobytes()
    ds.save_as(dcm_file_out)


# Main entry point of the test module
def main(args=sys.argv[1:]):
    print(f'Hello, I am the mercure test module')
    if len(sys.argv) < 3:
        print('Error: Missing arguments!')
        print('Usage: testmodule [input-folder] [output-folder]')
        sys.exit(1)

    in_folder = sys.argv[1]
    out_folder = sys.argv[2]
    if not Path(in_folder).exists() or not Path(out_folder).exists():
        print("IN/OUT paths do not exist")
        sys.exit(1)

    try:
        with open(Path(in_folder) / "task.json", "r") as json_file:
            task = json.load(json_file)
    except Exception:
        print('Error: Task file task.json not found')
        sys.exit(1)

    settings = { "sigma": 7, "series_offset": 1000 }
    if task.get("process",""):
        settings.update(task["process"].get("settings",{}))

    filecount = 0
    series = {}
    for entry in os.scandir(in_folder):
        if entry.name.endswith(".dcm") and not entry.is_dir():
            filecount += 1
            seriesString = entry.name.split("#", 1)[0]          
            if not seriesString in series.keys():
                series[seriesString] = []
            series[seriesString].append(entry.name)

    for item in series:
        series_uid = generate_uid()
        for image in series[item]:
            filename = image
            process_image(filename, in_folder, out_folder, series_uid, settings)


if __name__ == "__main__":
    main()
