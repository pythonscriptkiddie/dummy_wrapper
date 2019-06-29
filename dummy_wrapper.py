import cmd

showInstrumentation = True #prints the article in add_article

def add(dummy_argument):
    '''Dummy argument does nothing regardless of input'''
    if dummy_argument == '':
        add_article()
    else:
        add_article()

def add_article():
    '''Description of a news article'''
    title = input('Enter article title: ')
    link = input('Enter article url: ')
    description = input('Enter article description: ')
    article = {'title': title, 'link':link, 'description':description}
    if showInstrumentation == True:
        print(article)
    return article

class TestCMD(cmd.Cmd):
    intro = "Enter a command: add, quit"
    prompt = "(Command) "
    entry = ""
    
    def do_add(self, command):
        #command = input('Enter command: ')
        add(command)
        
    def do_quit(self, arg):
        print("Goodbye...")
        raise SystemExit
        
            
def main():
    app = TestCMD().cmdloop()
    
    
if __name__ == '__main__':
    main()
