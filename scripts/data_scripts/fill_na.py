import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 fill_na.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage2", "df_train.csv")
os.makedirs(os.path.join("data", "stage2"), exist_ok=True)

def process_data(fd_in, fd_out):
    arr_period_start = []
    arr_power = []
    arr_diffuse_radiation = []
    arr_direct_radiation = []
    arr_temperature_2m = []
    arr_windspeed_10m = []

    for line in fd_in:
        line = line.rstrip('\n').split(',')
        
        arr_period_start.append(line[0])
        if line[1]:
            arr_power.append(float(line[1]))
        else:
            arr_power.append(0)
        
        arr_diffuse_radiation.append(line[2])
        arr_direct_radiation.append(line[3])
        arr_temperature_2m.append(line[4])
        arr_windspeed_10m.append(line[5])

    for p_period_start, p_power, p_diffuse_radiation, p_direct_radiation, p_temperature_2m, p_windspeed_10m in zip(arr_period_start, arr_power, arr_diffuse_radiation, arr_direct_radiation, arr_temperature_2m, arr_windspeed_10m):
        fd_out.write("{},{},{},{}\n".format(p_period_start, p_power, p_diffuse_radiation, p_direct_radiation, p_temperature_2m, p_windspeed_10m))


with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)