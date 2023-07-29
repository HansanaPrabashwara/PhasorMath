import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from Phasor.phasor import Phasor
from SymmetricalComponents.unbalancedToSC import unbalancedToSC
from SymmetricalComponents.SCToUnbalanced import SCToUnbalanced


class Plot:
    def __init__(self,*phasor,theme = 0):
            self.phasor = phasor
            self.theme = theme
            self.fig = go.Figure()
            
            for i in phasor:
                self.__createTrace(i)
            
            self.fig.update_layout(template = self.__setTheme())
            self.fig.show(config={'modeBarButtonsToAdd': ['drawline',
                                        'drawopenpath',
                                        'drawclosedpath',
                                        'drawcircle',
                                        'drawrect',
                                        'eraseshape'
                                       ]})
       
        
    def __createTrace(self,phasor):
        if isinstance(phasor, Phasor):
            self.fig.add_trace(go.Scatterpolar(
                r = [0 , phasor.modulus],
                theta = [0 ,phasor.degree],
                # mode = 'lines',
                name = f'{phasor}',
                line_color = self.__color(phasor),
                mode="lines+markers",
                marker=dict(
                    symbol="arrow",
                    size=15,
                    angleref="previous",
                )       
            ))

        elif isinstance(phasor, unbalancedToSC):
            phasorNameSet = ("A","B","C")
            self.fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'polar'}]*3],subplot_titles=("Zero Sequence","Positive Sequence","Negative Sequence"))
            for i in range(3):
                for idx,j in enumerate(phasor.allComponents[i]):
                    self.fig.add_trace(go.Scatterpolar(
                        r = [0, j.modulus],
                        theta= [0,j.degree],
                        name = f'{phasorNameSet[idx]}{i} - {j}',
                        line_color = self.__color(phasorNameSet[idx]),
                        mode="lines+markers",
                        marker=dict(
                            symbol="arrow",
                            size=15,
                            angleref="previous",
                        ) 
                    ),1, i+1)

        elif isinstance(phasor, SCToUnbalanced):
            phasorNameSet = ("A","B","C")
            for idx,i in enumerate(phasor.unbalanced):
                self.fig.add_trace(go.Scatterpolar(
                    r = [0 , i.modulus],
                    theta = [0 ,i.degree],
                    # mode = 'lines',
                    name = f'{phasorNameSet[idx]} - {i}',
                    line_color = self.__color(phasorNameSet[idx]),
                    mode="lines+markers",
                    marker=dict(
                        symbol="arrow",
                        size=15,
                        angleref="previous",
                    )       
                ))

        else:
          raise TypeError(f"Unsupported operand type: {type(phasor)}")
        

    def __color(self,phasor):
        colorSet = [
            "black", "blue", "brown", "cadetblue", "chocolate", "coral", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod",
            "darkgray", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon",
            "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "deeppink", "dodgerblue", "firebrick",
            "forestgreen", "goldenrod", "gray", "grey", "green", "greenyellow", "indianred", "indigo", "khaki", "lavender", "lemonchiffon",
            "lightcoral", "lightgreen", "lightsalmon", "lightslategray", "lightslategrey", "lime", "mediumseagreen", "mediumslateblue",
            "mediumspringgreen", "midnightblue", "navy", "olive", "olivedrab", "orange", "orangered", "peru", "rosybrown", "royalblue",
            "saddlebrown", "sienna", "slategray", "slategrey", "steelblue", "tan", "teal", "thistle"
        ]

        return colorSet[phasor.__hash__()%len(colorSet)]

    def __setTheme(self):
        themes = ['plotly', 'plotly_white', 'plotly_dark','ggplot2', 'seaborn', 'simple_white', 'presentation', 'xgridoff', 'ygridoff', 'gridon', 'none']
        return themes[self.theme]


# "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure",
#                 "beige", "bisque", "black", "blanchedalmond", "blue",
#                 "blueviolet", "brown", "burlywood", "cadetblue",
#                 "chartreuse", "chocolate", "coral", "cornflowerblue",
#                 "cornsilk", "crimson", "cyan", "darkblue", "darkcyan",
#                 "darkgoldenrod", "darkgray", "darkgrey", "darkgreen",
#                 "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange",
#                 "darkorchid", "darkred", "darksalmon", "darkseagreen",
#                 "darkslateblue", "darkslategray", "darkslategrey",
#                 "darkturquoise", "darkviolet", "deeppink", "deepskyblue",
#                 "dimgray", "dimgrey", "dodgerblue", "firebrick",
#                 "floralwhite", "forestgreen", "fuchsia", "gainsboro",
#                 "ghostwhite", "gold", "goldenrod", "gray", "grey", "green",
#                 "greenyellow", "honeydew", "hotpink", "indianred", "indigo",
#                 "ivory", "khaki", "lavender", "lavenderblush", "lawngreen",
#                 "lemonchiffon", "lightblue", "lightcoral", "lightcyan",
#                 "lightgoldenrodyellow", "lightgray", "lightgrey",
#                 "lightgreen", "lightpink", "lightsalmon", "lightseagreen",
#                 "lightskyblue", "lightslategray", "lightslategrey",
#                 "lightsteelblue", "lightyellow", "lime", "limegreen",
#                 "linen", "magenta", "maroon", "mediumaquamarine",
#                 "mediumblue", "mediumorchid", "mediumpurple",
#                 "mediumseagreen", "mediumslateblue", "mediumspringgreen",
#                 "mediumturquoise", "mediumvioletred", "midnightblue",
#                 "mintcream", "mistyrose", "moccasin", "navajowhite", "navy",
#                 "oldlace", "olive", "olivedrab", "orange", "orangered",
#                 "orchid", "palegoldenrod", "palegreen", "paleturquoise",
#                 "palevioletred", "papayawhip", "peachpuff", "peru", "pink",
#                 "plum", "powderblue", "purple", "red", "rosybrown",
#                 "royalblue", "rebeccapurple", "saddlebrown", "salmon",
#                 "sandybrown", "seagreen", "seashell", "sienna", "silver",
#                 "skyblue", "slateblue", "slategray", "slategrey", "snow",
#                 "springgreen", "steelblue", "tan", "teal", "thistle", "tomato",
#                 "turquoise", "violet", "wheat", "white", "whitesmoke",
#                 "yellow", "yellowgreen"