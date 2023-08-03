from Phasor.sc import *
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from Phasor.phasor import *
from abc import abstractmethod


class Plot:
    """Generate polar plots to visualize Phasor objects, SCToUnbalanced objects, unbalancedToSC objects  
    """
    def __init__(self,*phasor,theme = 0):
        """Initialize Plot objects.

        Args:
            *phasor (Phasor/SCToUnbalanced/unbalancedToSC): phasor objects to visualize
            theme (int, optional): Theme selection. Defaults to 0.
        """
        self.phasor = phasor
        self.theme = theme
        self.fig = go.Figure()
        
        for i in phasor:
            self.createTrace(i)
        
        self.fig.update_layout(template = self.setTheme())
        self.fig.show(config={'modeBarButtonsToAdd': ['drawline',
                                    'drawopenpath',
                                    'drawclosedpath',
                                    'drawcircle',
                                    'drawrect',
                                    'eraseshape'
                                    ]})
    
    def createTrace(self,phasor):
        
        if isinstance(phasor, Phasor):
            self.fig = go.Figure()
            self.fig.add_trace(go.Scatterpolar(
                r = [0 , phasor.modulus],
                theta = [0 ,phasor.degree],
                name = f'{phasor}',
                showlegend=True,
                line_color = self.color(phasor),
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
                        line_color = self.color(phasorNameSet[idx]),
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
                    line_color = self.color(phasorNameSet[idx]),
                    mode="lines+markers",
                    marker=dict(
                        symbol="arrow",
                        size=15,
                        angleref="previous",
                    )       
                ))

        else:
          raise TypeError(f"Unsupported operand type: {type(phasor)}")
        

    def color(self,phasor):
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


    def setTheme(self):
        themes = ['plotly', 'plotly_white', 'plotly_dark','ggplot2', 'seaborn', 'simple_white', 'presentation', 'xgridoff', 'ygridoff', 'gridon', 'none']
        return themes[self.theme]


