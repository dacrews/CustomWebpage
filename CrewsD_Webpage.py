print('Welcome to the Personal Webpage Generator!\n')

def main():
    #gets information from the user
    name = input('What is your name?: ')
    degree = input('What is your degree major? ')
    career = input('What is your future career? Please write a brief description. ')

    #writes the HTML document
    def write_html():
        html_file.write('<html>\n')
        write_head()
        write_body()
        html_file.write('</html>\n')

    #writes the head and title portions of the HTML document
    def write_head():
        html_file.write('<head>\n')
        html_file.write('<title> My Personal Webpage Generator </title>\n')
        html_file.write('</head>\n')

    #writes the body portion of the HTML code and adds the information entered by the user
    def write_body():
        html_file.write('<body>\n')
        html_file.write('<center>\n')
        html_file.write('<h1>' + name + '</h1>\n')
        html_file.write('<hr/>\n')
        html_file.write('<h2>' + degree + '</h2>\n')
        html_file.write('<hr/>\n')
        html_file.write(career + '\n')
        html_file.write('</center>\n')
        html_file.write('<hr/>\n')
        html_file.write('</body>\n')

    #creates and writes to the HTML file
    html_file = open('CrewsD_Webpage.html', 'w')
    write_html()
    html_file.close()

#calls the main function
main()
