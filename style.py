from utils import print_errors


def set_brace_style(file_path, style_indent):
    with open(file_path, 'r') as file:
        opening_braces = 0
        closing_braces = 0
        errors = []
        for line_number, line in enumerate(file, start=1):
            opening_braces += line.count("{")
            closing_braces += line.count("}")

            if "{" in line:
                if style_indent == '':
                    if line[0][0] == "{":
                        style_indent = 'allman'
                    elif line.split()[0][0] == "{":
                        style_indent = 'gnu'
                    elif line.split()[-1][-1] == "{":
                        style_indent = 'kernel'
                    else:
                        errors.append("Единый стиль форматирования не найден!")
                        break

        if opening_braces != closing_braces:
            errors.append("Ошибка: количество открывающихся и закрывающихся фигурных скобок не совпадает!")
        print_errors(errors)
        print("Стиль форматирования: " + style_indent + " style")
        return style_indent


def check_brace_style(code, style):
    with open(code, 'r') as file:
        error_lines = []
        if style == 'allman' or style == 'gnu':
            for i, line in enumerate(file):
                line = line.rstrip()
                if '{' in line and '};' in line:
                    continue
                elif '{' in line and not line.strip() == '{':
                    error_lines.append("Строка " + str(
                        i + 1) + " : Фигурная скобка должна быть отформатирована согласно стилю!")
                elif '}' in line and not line.strip().startswith('}'):
                    error_lines.append("Строка " + str(
                        i + 1) + " : Фигурная скобка должна быть отформатирована согласно стилю!")
        # elif style == "gnu":
        #     indent_level = 1
        #
        #     for i, line in enumerate(file):
        #         statement_exist = 'for' in line or 'if' in line or 'while' in line or 'else' in line
        #         line = line.rstrip()
        #         if '{' in line and '};' in line:
        #             continue
        #         elif '{' in line and line.strip() == '{':
        #             if not line == indent_level * size_indent * ' ' + '{':
        #                 error_lines.append("Строка " + str(
        #                     i + 1) + " : Фигурная скобка должна быть отформатирована согласно стилю!")
        #             indent_level += 2
        #         elif '}' in line and line.strip() == '}':
        #             indent_level -= 2
        #             if not line == indent_level * size_indent * ' ' + '}':
        #                 error_lines.append("Строка " + str(
        #                     i + 1) + " : Фигурная скобка должна быть отформатирована согласно стилю!")
        #         elif statement_exist:
                    pass
        elif style == "kernel":
            for i, line in enumerate(file):
                line = line.rstrip()
                if '{' in line and '};' in line:
                    continue
                elif '{' in line and (not line.strip().endswith('{') or line.strip() == '{'):
                    error_lines.append("Строка " + str(
                        i + 1) + " : Фигурная скобка должна быть отформатирована согласно стилю!")
                elif '}' in line and not line.strip().startswith('}'):
                    error_lines.append("Строка " + str(
                        i + 1) + " : Фигурная скобка должна быть отформатирована согласно стилю!")
    print_errors(error_lines)
    return
