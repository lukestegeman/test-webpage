import openpyxl

if __name__ == '__main__':
    

    # READ MODEL LIST FILE
    filename = 'model-list.txt'
    a = open(filename, 'r')
    read = a.readlines()
    a.close()
    

    category_marker = ':~:'

    model_dict = {}
    
    for i in range(0, len(read)):
        line = read[i].rstrip('\n')
        if category_marker in line:
            category = line.split(category_marker)[0]
            model_dict[category] = []
        else:
            model_dict[category].append(line)
   
    # CREATE NEW CHECKBOX STRING
    checkbox_string = ''
    spreadsheet_list = []
    for category, models in model_dict.items():
        checkbox_string += '<br><br><div class="info-text">' + category + ' Models</div>\n'
        for model in models:
            checkbox_string += '            <label>\n'
            checkbox_string += '                <input name="' + model + '" type="checkbox" id="' + model + '" value="1">\n'
            checkbox_string += '                <span>' + model + '</span>\n'
            checkbox_string += '            </label>\n'
            spreadsheet_list.append(model)
 

    # REPLACE ${checkboxes}$ IN index_template.html
    a = open('index_template.html', 'r')
    read = a.read()
    a.close()

    write_string = read.replace('${checkboxes}$', checkbox_string)
    a = open('index.html', 'w')
    a.write(write_string)
    a.close()


    # WRITE TO EXCEL SPREADSHEET; COPYPASTE TO GOOGLE SHEETS
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for index, value in enumerate(spreadsheet_list, start=1):
        sheet.cell(row=1, column=index, value=value)
    workbook.save('model-columns.xlsx')
    workbook.close()
    
    print('Copy and paste the values in model-columns.xlsx to the model columns in mailsphinx-subscriber-data (https://docs.google.com/spreadsheets/d/1PJlkhI0aimpJH2o7KaN62-Lx0Hp_e-DQoPqi8KjiEC4/edit?gid=0#gid=0)')
    





