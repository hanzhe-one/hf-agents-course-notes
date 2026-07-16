"""
multiAgent.py — 多工具 CodeAgent（对齐 HF Agents Course · Unit 2 · smolagents）
Multi-tool CodeAgent, aligned with HF Agents Course · Unit 2 · smolagents.

课程出处 / Source: https://huggingface.co/learn/agents-course

课程示例：Alfred 需要查找蝙蝠侠取景地并估算货机转运时间。
这里保留课程的 calculate_cargo_travel_time 工具 + 搜索/访问网页工具，
模型换成 HF serverless Inference（InferenceClientModel）。
pip install "smolagents[toolkit]" pandas
Run 前在根目录 .env 配置：HUGGINGFACEHUB_API_TOKEN=hf_xxx
"""

import math
import os
from typing import Optional, Tuple

from dotenv import load_dotenv
from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    InferenceClientModel,
    VisitWebpageTool,
    tool,
)

load_dotenv()


@tool
def calculate_cargo_travel_time(
    origin_coords: Tuple[float, float],
    destination_coords: Tuple[float, float],
    cruising_speed_kmh: Optional[float] = 750.0,  # 货机的平均巡航速度
) -> float:
    """Calculate the travel time for a cargo plane between two points on Earth using great-circle distance.

    Args:
        origin_coords: Tuple of (latitude, longitude) for the starting point
        destination_coords: Tuple of (latitude, longitude) for the destination
        cruising_speed_kmh: Optional cruising speed in km/h (defaults to 750 km/h for typical cargo planes)

    Returns:
        float: The estimated travel time in hours

    Example:
        >>> # Chicago (41.8781° N, 87.6298° W) to Sydney (33.8688° S, 151.2093° E)
        >>> result = calculate_cargo_travel_time((41.8781, -87.6298), (-33.8688, 151.2093))
    """

    def to_radians(degrees: float) -> float:
        return degrees * (math.pi / 180)

    lat1, lon1 = map(to_radians, origin_coords)
    lat2, lon2 = map(to_radians, destination_coords)

    EARTH_RADIUS_KM = 6371.0

    # 半正矢公式（Haversine）计算大圆距离
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.asin(math.sqrt(a))
    distance = EARTH_RADIUS_KM * c

    # 增加 10% 以考虑非直线航路与空管
    actual_distance = distance * 1.1
    # 为起降程序额外增加 1 小时
    flight_time = (actual_distance / cruising_speed_kmh) + 1.0
    return round(flight_time, 2)


def main():
    model = InferenceClientModel(
        model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
        token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    )

    task = (
        "Find all Batman filming locations in the world, calculate the time to "
        "transfer via cargo plane to here (we're in Gotham, 40.7128° N, 74.0060° W), "
        "and return them to me as a pandas dataframe.\n"
        "Also give me some supercar factories with the same cargo plane transfer time."
    )

    agent = CodeAgent(
        tools=[DuckDuckGoSearchTool(), VisitWebpageTool(), calculate_cargo_travel_time],
        model=model,
        additional_authorized_imports=["pandas"],
        max_steps=15,
    )
    result = agent.run(task)
    print(result)


if __name__ == "__main__":
    main()
