"""Demonstrates usage of the timeline tool."""

import matplotlib.pyplot as plt
import pandas as pd
from .timeline import get_timeline


def main() -> None:
    data = [
        ["08/21/2022", "", "this is a milestone", 5, {}],
        ["2022-08-21 08:00", "", "this is another milestone", 4, {}],
        [
            "2022-08-21 10:00",
            "",
            "this is a milestone with a very, very long description that "
            "we will want to wrap into multiple lines",
            3,
            {"text_wrap": 30},
        ],
        [
            "2022-08-20 12:00",
            "2022-08-22 12:00",
            'this is a "span", indicating an activity that ocurrs over a period of time',
            6,
            {"text_wrap": 300, "color": "red", "alpha": 0.5},
        ],
        [
            "2022-08-21 12:00",
            "2022-08-21 23:00",
            "another span",
            7,
            {"color": "yellow"},
        ],
        [
            "2022-08-22 12:00",
            "",
            "something interesting happens here (a milestone without a vertical line)",
            6,
            {
                "vline": False,
                "y_offset": -30,
                "x_offset": -40,
                "color": "green",
                "arrowprops": {
                    "arrowstyle": "->",
                    "connectionstyle": "arc3,rad=0.1",
                    "shrinkB": 5,
                },
            },
        ],
        ["2022-08-22 16:00", "", "Something happens later", 2, {}],
    ]
    d = pd.DataFrame(data, columns=["start", "end", "description", "height", "options"])

    ax = get_timeline(d, filename="timeline-1.png")

    d.at[3, "options"].update({"annotation_anchor": "start", "x_offset": 200})
    d.at[2, "options"].update({"horizontalalignment": "right", "x_offset": -10})
    d.at[6, "options"].update(
        {
            "marker": False,
            "annotation_anchor": "end",
            "text_wrap": 10,
            "x_offset": -100,
            "arrowprops": {
                "arrowstyle": "->",
                "shrinkB": 5,
                "relpos": (1, 1),
                "connectionstyle": "arc3,rad=-0.1",
            },
        }
    )
    ax = get_timeline(
        d,
        start="2022-08-21 06:00",
        end="2022-08-21 11:00",
        interval=1,
        dateformat="%b %d %H:%M",
    )

    plt.show()


if __name__ == "__main__":
    main()
