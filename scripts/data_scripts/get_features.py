import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython3 get_features.py data-file\n")
    sys.exit(1)

f_input = sys.argv[1]
f_output = os.path.join("data", "stage1", "df_train.csv")
os.makedirs(os.path.join("data", "stage1"), exist_ok=True)

def process_data(fd_in, fd_out):
    fd_in.readline()
    for line in fd_in:
        line = line.rstrip('\n').split(',')
        p_period_start = line[0]
        p_power = line[1]
        p_diffuse_radiation = line[6]
        p_direct_radiation = line[8]
        p_temperature_2m = line[11]
        p_windspeed_10m = line[14]
        
        fd_out.write("{},{},{},{}\n".format(p_period_start, p_power, p_diffuse_radiation, p_direct_radiation, p_temperature_2m, p_windspeed_10m))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)