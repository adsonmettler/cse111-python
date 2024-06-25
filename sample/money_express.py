"""
Author: Anderson Mettler do Nascimento

Dependencies: This program uses the python modules "tkinter" and "tkcalendar" which
do not always come preinstalled in python3. If it is not installed on your computer
you will need to run the following 2 commands on your terminal:

    sudo apt install python3-tk
    pip3 install tkcalendar

This program also uses the FloatEntry class from the number_entry module. The 
number_entry.py file must be in the same folder as money_express.py.
"""

import requests
import json
import tkinter as tk
from tkinter import Frame, Label, Button
from tkinter.ttk import Separator
from tkcalendar import DateEntry
from number_entry import FloatEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Money Express")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)
    
    root.mainloop()


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Date:"
    lbl_date = Label(frm_main, text="Date:")

    # Create an calendar entry box where the user will enter the date.
    ent_date = DateEntry(frm_main, date_pattern="dd-mm-yyyy")
    # ent_date.pack()

    # Create an float entry box where the user will enter the BRL amount to convert.
    ent_brl = FloatEntry(frm_main, width=4, lower_bound=0.0001, upper_bound=999999)

    # Create an float entry box where the user will enter the USD amount to convert.
    ent_usd = FloatEntry(frm_main, width=4, lower_bound=0.0001, upper_bound=999999)

    # Create a label that displays "1 USD ="
    lbl_1usd = Label(frm_main, text="1 USD =")

    # Create a label that displays "1 BRL ="
    lbl_1brl = Label(frm_main, text="1 BRL =")

    # Create a label that displays "CONVERT:"
    lbl_convert = Label(frm_main, text="CONVERT")

    # Create labels that will display the results.
    lbl_brl_rate = Label(frm_main, width=3)
    lbl_usd_rate = Label(frm_main, width=3)
    lbl_brl_units = Label(frm_main, text="BRL")
    lbl_usd_units = Label(frm_main, text="USD")

    # Create a Separator"
    separator = Separator(frm_main, orient='horizontal')

    lbl_brl = Label(frm_main, text="BRL:")
    lbl_usd = Label(frm_main, text="USD:")
    lbl_message = Label(frm_main, text="Message:")
    lbl_message_display = Label(frm_main, text="Welcome!")

    # Create the Get Rate button.
    btn_get_rate = Button(frm_main, text="Get Rate")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_date.grid(      row=0, column=0, padx=3, pady=3)
    ent_date.grid(      row=0, column=1, padx=0, pady=3)
    btn_get_rate.grid(  row=0, column=3, padx=3, pady=3, columnspan=4, sticky="w")

    lbl_1usd.grid(     row=1, column=0, padx=(30,3), pady=3)
    lbl_brl_rate.grid( row=1, column=1, padx=3, pady=3, sticky='ew')
    lbl_brl_units.grid(row=1, column=2, padx=0, pady=3)

    lbl_1brl.grid(     row=2, column=0, padx=(30,3), pady=3)
    lbl_usd_rate.grid( row=2, column=1, padx=3, pady=3, sticky='ew')
    lbl_usd_units.grid(row=2, column=2, padx=0, pady=3)

    separator.grid(row=3, column=0, sticky='ew', columnspan=7)

    lbl_convert.grid(  row=4, column=1, padx=3, pady=3)

    lbl_usd.grid(      row=5, column=0, padx=0, pady=3)
    ent_usd.grid(      row=5, column=1, padx=3, pady=3, sticky='ew')

    lbl_brl.grid(      row=6, column=0, padx=0, pady=3)
    ent_brl.grid(      row=6, column=1, padx=3, pady=3, sticky='ew')

    lbl_message.grid(  row=7, column=0, padx=0, pady=3)
    lbl_message_display.grid(row=7, column=1, padx=3, pady=3, sticky='ew')


    # This function will be called each time the user releases a key
    # in the ent_brl field.
    def convert_to_usd(event):
        """Converts BRL to USD displays the result.
        """
        try:
            # Get the BRL rate.
            value_usd = lbl_brl_rate.cget("text")

            # Compute the BRL valeu.
            value_brl = convert_currency(float(value_usd), float(ent_brl.get()))

            # Updates the UI with the new converted value
            ent_usd.set(value_brl)

        except ValueError:
            print(ValueError)

    # This function will be called each time the user releases a key
    # in the ent_usd field.
    def convert_to_brl(event):
        """Converts USD to BRL and displays the result.
        """
        try:
            # Get the USD rate.
            value_brl = lbl_usd_rate.cget("text")

            # Compute the USD valeu.
            value_usd = convert_currency(float(value_brl), float(ent_usd.get()))

            # Updates the UI with the new converted value
            ent_brl.set(value_usd)

        except ValueError:
            print(ValueError)


    # This function will be called each time
    # the user presses the "get_rate" button.
    def get_rate():
        """Calls the request_dollar_rate fucntion, extracts the
        dollar rate from the JSON response and updates the UI
        with the correct values."""
        btn_get_rate.focus()
        lbl_message_display.config(text='')
        date = ent_date.get_date()
        date = date.strftime("%m-%d-%Y")
        ent_brl.clear()
        ent_usd.clear()
        lbl_brl_rate.config(text='')
        lbl_usd_rate.config(text='')

        data_dict = request_dollar_rate(date)
        print(data_dict)

        try:
            usd_value = data_dict['value'][0]['cotacaoCompra']
        except  IndexError as index_err:
            lbl_message_display.config(text='Rate unavailable.\nChose other date')

        brl_value = 1 / usd_value
        lbl_brl_rate.config(text=f'{brl_value:.4f}')
        lbl_usd_rate.config(text=f'{usd_value:.4f}')
        ent_usd.focus()

    # Bind the convert functions to the entry boxes so
    # that the computer will call the convert functions
    # when the user changes the text in the entry boxes.
    ent_brl.bind("<KeyRelease>", convert_to_usd)
    ent_usd.bind("<KeyRelease>", convert_to_brl)

    # Bind the get_rate function to the Get Rate button so
    # that the computer will call the get_rate function
    # when the user clicks the button.
    btn_get_rate.config(command=get_rate)

    # Give the keyboard focus to the ent_usd entry box.
    ent_usd.focus()


def request_dollar_rate(date):
    """Makes an http GET request to Banco Central API
    using the give date and gets the BRL-USD rate for
    that date.

    Parameters
        date: date to use in the request. Needs to be
        in the format mm-dd-yyyy.
        
    Return: a dictionary with all the data from
     the API call response.
    """

    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao='{date}')"
    payload = {}
    headers = {}
    # print(url)

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    return generate_dic_from_response(response)


def convert_currency(value, rate):
    """Converts a given ammount in the source corrency
    to the new currency.

    Parameters
        value: the amount in the source currency that 
        needs to be convered to the new currency.
        rate: the value of 1 unit of the source currency in the
        new currency.
        
    Return: the amount in the new currency.
    """
    return value * rate

def generate_dic_from_response(response):
    """Makes an http GET request to Banco Central API
    using the give date and gets the BRL-USD rate for
    that date.

    Parameters
        response: the full API call response.
        
    Return: a dictionary with all the data from
     the API call response.
    """
    dictionary = json.loads(response.text)
    return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()