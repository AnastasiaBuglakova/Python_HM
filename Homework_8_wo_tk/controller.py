
import model_calc
import view
import model_calc as mc
def start():
    while True:
        line_str = view.launch()
        entered_str = line_str
        if '(' in line_str:
            line_str = view.bracket(line_str)
            while '(' in line_str:
                entered_str = line_str
                line_inside_bracket = mc.bracket_fun(line_str)

                arifmet_result_list = mc.parse(line_inside_bracket)

                if view.div_by_zero(arifmet_result_list):
                    view.error_warning(0)
                    result = 'error'
                else:
                    arifmet_result_str = mc.arifmitic(arifmet_result_list)

                    line_str = entered_str.replace(('(' + line_inside_bracket + ')'), str(arifmet_result_str))

        if len(line_str) > 1:
            entered_list = mc.parse(line_str)

            if view.div_by_zero(entered_list):
                view.error_warning(0)
                result = 'error'
            else:
                result = mc.arifmitic(entered_list)
        else:
            result = entered_list
        view.show_result(result)

