class TableFormatter():
    def headings(self,headers):
        raise NotImplementedError()
    def row(self, rowdata):
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfoio data in CSV format.
    '''

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HtmlTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')    
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HtmlTableFormatter()
    else:
        raise FormatError(f'Unknown table format \'{fmt}\'')

def print_table(data, whatshow, formatter):
    formatter.headings(whatshow)
    for info in data:
        rowdata = [ str(getattr(info, col)) for col in whatshow]
        formatter.row(rowdata)
