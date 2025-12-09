import { Chart } from "chart.js";
import { onMount } from "svelte";
import type { ConnectionManager } from "./connectionManager.svelte";

export function applyChartHooks(
    chartCanvasElement: () => HTMLCanvasElement | null,
    chartSetter: (x: Chart) => void,
    getCm: () => (ConnectionManager | null),
    chart: () => (Chart | null),
) {
    onMount(() => {
        const ctx = chartCanvasElement()?.getContext('2d');
        if (ctx) {
            const chart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ["daddad", "adad"],
                    datasets: [{
                        label: 'Detection Confidence',
                        data: [50, 50],
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    animation: false,
                    scales: {
                        y: {
                            beginAtZero: true,
                        }
                    }
                }
            });
            chartSetter(chart);
            return () => {
                chart?.destroy();
            }
        }
    })

    $effect(() => {
        const cm = getCm();
        const currentChart = chart();
        if (cm && currentChart) {
            const detectionStats = cm.detectionStats;
            currentChart.data.labels = Object.keys(detectionStats.confidences);
            currentChart.data.datasets[0].data = Object.values(detectionStats.confidences);
            currentChart.update();
        }
    })
}