import React from 'react';
import { VictoryPie } from 'victory';

function StatusPieChart(props) {
    return (
        <VictoryPie
            colorScale={["rgb(211,59,55)", "rgb(30,148,78)", "rgb(253,197,54)"]}
            padding={20}
            style={{
                data: { strokeWidth: 0 }
            }}
            innerRadius={75}
            labels={() => null}
            animate={{ duration: 2000 }}
            data={[
                { y: props.red },
                { y: props.green },
                { y: props.yellow }
            ]}
        />
    )
}

export { StatusPieChart };