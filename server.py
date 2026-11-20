"""CGPA MCP server (Task 1). Run:  python server.py  ->  http://127.0.0.1:8000/mcp"""
from fastmcp import FastMCP
from tools import (
    marks_to_grade_points,
    calculate_semester_gpa,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_semester_courses,
    get_remaining_credit_hours,
    save_report,
)
mcp = FastMCP("cgpa")
for fn in (
    marks_to_grade_points,
    calculate_semester_gpa,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_semester_courses,
    get_remaining_credit_hours,
    save_report,
):
    mcp.tool(fn)

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)