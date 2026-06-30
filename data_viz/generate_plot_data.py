from star_gate.stargate_module import StarGate
import json

def generate_plot_data(source, y_col, x_col="index", output="star_file.json"):
    data = StarGate()
    data.read(source)

    # if isinstance(data, dict):
    #     df = list(data.values())[1]
    # else :
    #     df = data

    # y = df[y_col].tolist()

    # if x_col != "index":
    #     x = df[x_col].tolist()
    # else :
    #     x = list(range(len(y)))
    
    # result = {
    #     "x" : x,
    #     "y" : y
    # }

    # with open(output, "w") as f :
    #     json.dump(result, f, indent=2)
    
    json.dump(data.to_json(), output)
    
    print(f"JSON genere : {output}")

def star_to_json(star_file_path, json_file_path):
    data_blocks = {}
    current_block = None
    columns = []
    rows = []
    in_loop = False

    with open(star_file_path, 'r') as f:
        for line in f:
            line = line.strip()

            # Ignorer lignes vides et commentaires
            if not line or line.startswith('#'):
                continue

            # Nouveau bloc data_
            if line.startswith('data_'):
                if current_block and rows:
                    data_blocks[current_block] = rows
                current_block = line
                columns = []
                rows = []
                in_loop = False

            # Début d'un loop
            elif line.startswith('loop_'):
                in_loop = True
                columns = []
                rows = []

            # Colonnes
            elif line.startswith('_'):
                columns.append(line)

            # Données
            elif in_loop:
                values = line.split()
                if len(values) == len(columns):
                    row_dict = dict(zip(columns, values))
                    rows.append(row_dict)

        # Sauvegarder dernier bloc
        if current_block and rows:
            data_blocks[current_block] = rows

    # Écriture JSON
    with open(json_file_path, 'w') as f:
        json.dump(data_blocks, f, indent=4)

    print(f"Conversion terminée : {json_file_path}")

if __name__ == "__main__" :
    # generate_plot_data(
    #     source="./data_viz/corrected_micrographs.star",
    #     y_col="rlnAccumMotionTotal"
    # )

    star_to_json("data_viz/corrected_micrographs.star", "data_viz/star_file.json")
    # data = starfile.read("public/spa/02_preprocess/corrected_micrographs.star")

    # if isinstance(data, dict):
    #     for key in data:
    #         print("TABLE : ", key)
    #         print(data[key].columns)
    # else :
    #     print(data.columns)