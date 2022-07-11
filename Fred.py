import numpy as np
import pandas as pd


class Fred:

    @staticmethod
    def run(
        count: int
    ) -> pd.DataFrame:

        np.random.seed()

        dfs = []

        c = 0
        d = 0
        for x in [-0.5, 0.5]:
            for y in [-0.5, 0.5]:

                dx = np.random.normal(
                    x, 
                    0.25, 
                    count
                )

                dy = np.random.normal(
                    y, 
                    0.25, 
                    count
                )

                df = pd.DataFrame(
                    pd.DataFrame(
                        {
                            'x': dx, 
                            'y': dy
                        }
                    )
                )

                df['c'] = c
                df['d'] = 0 if d==0 or d==3 else 1

                dfs.append(df)

                c += 1
                d += 1

        return pd.concat(
            dfs,
            ignore_index=True
        )

print(Fred.run(100).head())