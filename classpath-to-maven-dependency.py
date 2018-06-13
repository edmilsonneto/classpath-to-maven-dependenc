import codecs

def extractFileName(line):
    array = line[38:-4].split("/")
    lenght =  len(array)
    return array[lenght - 1]

def readFile():
    with codecs.open("/Users/edmilsonneto/Desktop/classpath.xml", "r", "utf-8") as sourceFile:
        lines = sourceFile.readlines()
        for line in lines:
            writeLine(line)

def writeLine(line):
    fileName = extractFileName(line)

    with open('/Users/edmilsonneto/Desktop/output.xml', 'a') as the_file:
        the_file.write('<dependency>\n')
        the_file.write('<groupId>' + fileName + '</groupId>\n')
        the_file.write('<artifactId>' + fileName + '</artifactId>\n')
        the_file.write('<version>' + fileName + '</version>\n')
        the_file.write('<scope>system</scope>\n')
        the_file.write('<systemPath> $''{''project.basedir''}''/src/main/webapp/WEB-INF/lib/' + fileName + ' </systemPath>\n\n')


readFile()