import PySimpleGUI as sg
from tabulate import tabulate

cars = []

# Car Inventory
TG_Enterprises = [
    ['1', 'CULTUS', '4', '3500', '300', '550'],
    ['2', 'SONATA', '3', '5000', '350', '750'],
    ['3', 'KIA Sportage', '3', '6000', '500', '700'],
    ['4', 'Yaris', '5', '4000', '300', '600'],
    ['5', 'HONDA CIVICS', '5', '5500', '300', '600'],
    ['6', 'Pajero', '2', '7000', '500', '700']
]

sg.theme('Purple')

#main layout
layout1 = [
    [sg.Text("Select a function:")],
    [sg.Button("Car Rental", key="-RENTAL-")],
    [sg.Button("Car Return", key="-RETURN-")],
    [sg.Button("Total Finance Detail", key="-TFD-")]
]

Text = [
    [sg.Text("TG ENTERPRISES", font="bold", justification="centre", text_color="purple", size=(600, 100))]
]

layout = [
    [sg.Column(layout1), sg.VSeperator(), sg.Column(Text)]
]

window = sg.Window('TG Enterprises', layout, size=(800, 200))

# main event
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    # rental window
    elif event == "-RENTAL-":
        headings = ['Car no.', 'Model', 'Available', 'Price/Day', 'Liability Insurance/Day', 'Comprehensive Insurance/Day']

        Consistant = [
            [sg.Text("Select a function:")],
            [sg.Button("Car Rental", key="-RENTAL-")],
            [sg.Button("Car Return", key="-RETURN-")],
            [sg.Button("Total Finance Detail", key="-TFD-")]
        ]

        Table_text = [
            [sg.Text("TG ENTERPRISES", font="bold", justification="centre", text_color="purple")],
            [sg.Text("Select a car:")],
            [sg.Table(values=TG_Enterprises, headings=headings, max_col_width=35,
                      auto_size_columns=True, justification='right', num_rows=7,
                      enable_events=True, key='-TABLE-', row_height=35)],
            [sg.Text("Enter number of days:"), sg.Input(key="-DAY-", size=(20, 1))],
            [sg.Text("Insurance Type:")],
            [sg.Radio("Liability", "RADIO", key="-LIABILITY-")],
            [sg.Radio("Comprehensive", "RADIO", key="-COMPREHENSIVE-")],
            [sg.Ok()]
        ]

        layout2 = [[sg.Column(Consistant), sg.VSeperator(), sg.Column(Table_text)]]
        window2 = sg.Window("TG Enterprise", layout2)

        while True:
            event2, values2 = window2.read()
            if event2 in (sg.WIN_CLOSED, "Exit"):
                break
            if event2 == "-TABLE-":
                try:
                    car_index = values2[event2][0]
                    car_name = TG_Enterprises[car_index][1]
                    car_available = int(TG_Enterprises[car_index][2])
                    days = int(values2["-DAY-"])

                    insurance_type = "-LIABILITY-" if values2["-LIABILITY-"] else "-COMPREHENSIVE-"
                    rental_cost = int(TG_Enterprises[car_index][3]) * days

                    if values2["-LIABILITY-"]:
                        rental_cost += int(TG_Enterprises[car_index][4]) * days
                    else:
                        rental_cost += int(TG_Enterprises[car_index][5]) * days

                    TG_Enterprises[car_index][2] = str(car_available - 1)
                    cars.append([car_name, days, rental_cost, insurance_type])
                except:
                    sg.popup_error("Fill all fields and select a car.")

            elif event2 == "Ok":
                window2.close()
                break

        window2.close()

    # return window
    elif event == "-RETURN-":
        if not cars:
            sg.popup("No cars are currently rented.", title="Return")
        else:
            return_data = [f"{i+1}. {car[0]} - {car[1]} days - PKR {car[2]} - {car[3]}" for i, car in enumerate(cars)]
            return_layout = [
                [sg.Text("Select a car to return:")],
                [sg.Listbox(values=return_data, size=(50, 6), key="-RETURN-CAR-", enable_events=True)],
                [sg.Button("Return"), sg.Button("Cancel")]
            ]
            return_window = sg.Window("Return Car", return_layout)

            while True:
                ret_event, ret_values = return_window.read()
                if ret_event in (sg.WIN_CLOSED, "Cancel"):
                    break
                if ret_event == "Return":
                    try:
                        index = int(ret_values["-RETURN-CAR-"][0].split('.')[0]) - 1
                        car_name = cars[index][0]
                        # Optional: increase car availability
                        for entry in TG_Enterprises:
                            if entry[1] == car_name:
                                entry[2] = str(int(entry[2]) + 1)
                                break
                        cars.pop(index)
                        sg.popup("Car returned successfully.")
                        break
                    except:
                        sg.popup_error("Please select a car to return.")
            return_window.close()
#Finance 
    elif event == "-TFD-":
        if not cars:
            sg.popup("No cars have been rented yet.")
        else:
            headers = ['Car', 'Days', 'Total Cost', 'Insurance']
            table = tabulate(cars, headers=headers, tablefmt="pretty")
            total_cost = sum([int(c[2]) for c in cars])
            sg.popup_scrolled(f"Rental Summary:\n\n{table}\n\nTotal Income: PKR {total_cost}", title="Finance Detail")

window.close()
