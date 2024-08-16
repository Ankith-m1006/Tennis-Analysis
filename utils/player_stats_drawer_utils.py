import numpy as np
import cv2
import pandas as pd
from fpdf import FPDF
import os
import matplotlib.pyplot as plt

def determine_shot_type(speed):
    # Define speed thresholds for different shot types
    if speed > 35:
        return "Power Shot"
    elif speed > 25:
        return "Fast"
    elif speed > 15:
        return "Medium"
    else:
        return "Slow"

def draw_player_stats(output_video_frames, player_stats):
    for index, row in player_stats.iterrows():
        player_1_shot_speed = row['player_1_last_shot_speed']
        player_2_shot_speed = row['player_2_last_shot_speed']
        player_1_speed = row['player_1_last_player_speed']
        player_2_speed = row['player_2_last_player_speed']

        avg_player_1_shot_speed = row['player_1_average_shot_speed']
        avg_player_2_shot_speed = row['player_2_average_shot_speed']
        avg_player_1_speed = row['player_1_average_player_speed']
        avg_player_2_speed = row['player_2_average_player_speed']

        # Check if frame exists
        if index >= len(output_video_frames):
            print(f"Index {index} is out of bounds for output_video_frames.")
            continue

        frame = output_video_frames[index]
        
        # Check if frame is None or not a valid image
        if frame is None:
            print(f"Frame at index {index} is None.")
            continue
        if len(frame.shape) != 3:
            print(f"Frame at index {index} does not have the expected 3 dimensions: {frame.shape}")
            continue

        height, width, _ = frame.shape

        start_x = width - 400
        start_y = height - 500
        end_x = start_x + 360
        end_y = start_y + 270

        overlay = frame.copy()
        cv2.rectangle(overlay, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)
        alpha = 0.5
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
        output_video_frames[index] = frame

        text = "     Player 1     Player 2"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 80, start_y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        text = "Shot Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 10, start_y + 80), cv2.FONT_HERSHEY_COMPLEX, 0.45, (255, 255, 255), 1)
        text = f"{player_1_shot_speed:.1f} km/h    {player_2_shot_speed:.1f} km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 130, start_y + 80), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2)

        text = "Player Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 10, start_y + 120), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        text = f"{player_1_speed:.1f} km/h    {player_2_speed:.1f} km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 130, start_y + 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        text = "avg. S. Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 10, start_y + 160), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        text = f"{avg_player_1_shot_speed:.1f} km/h    {avg_player_2_shot_speed:.1f} km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 130, start_y + 160), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        text = "avg. P. Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 10, start_y + 200), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        text = f"{avg_player_1_speed:.1f} km/h    {avg_player_2_speed:.1f} km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 130, start_y + 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        player_1_shot_type = determine_shot_type(player_1_shot_speed)
        player_2_shot_type = determine_shot_type(player_2_shot_speed)
        text = f"Shot Type: {player_1_shot_type}        Shot Type: {player_2_shot_type}"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x + 10, start_y + 240), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)

    return output_video_frames

def generate_pdf_report(player_stats, output_path="player_performance_report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Add Title Page
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Player Performance Evaluation", ln=True, align="C")
    pdf.ln(20)

    # Calculate averages
    avg_stats = player_stats.mean()

    # Add Performance Summary
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Overall Performance Summary:", ln=True)
    pdf.ln(5)

    # Player 1 Stats
    pdf.cell(0, 10, f"Player 1 Average Shot Speed: {avg_stats['player_1_last_shot_speed']:.1f} km/h", ln=True)
    pdf.cell(0, 10, f"Player 1 Average Speed: {avg_stats['player_1_last_player_speed']:.1f} km/h", ln=True)
    pdf.cell(0, 10, f"Player 1 Average Shot Speed (All Frames): {avg_stats['player_1_average_shot_speed']:.1f} km/h", ln=True)
    pdf.cell(0, 10, f"Player 1 Average Speed (All Frames): {avg_stats['player_1_average_player_speed']:.1f} km/h", ln=True)

    # Player 2 Stats
    pdf.cell(0, 10, f"Player 2 Average Shot Speed: {avg_stats['player_2_last_shot_speed']:.1f} km/h", ln=True)
    pdf.cell(0, 10, f"Player 2 Average Speed: {avg_stats['player_2_last_player_speed']:.1f} km/h", ln=True)
    pdf.cell(0, 10, f"Player 2 Average Shot Speed (All Frames): {avg_stats['player_2_average_shot_speed']:.1f} km/h", ln=True)
    pdf.cell(0, 10, f"Player 2 Average Speed (All Frames): {avg_stats['player_2_average_player_speed']:.1f} km/h", ln=True)

    # Determine average shot types
    avg_player_1_shot_type = determine_shot_type(avg_stats['player_1_last_shot_speed'])
    avg_player_2_shot_type = determine_shot_type(avg_stats['player_2_last_shot_speed'])

    pdf.cell(0, 10, f"Player 1 Average Shot Type: {avg_player_1_shot_type}", ln=True)
    pdf.cell(0, 10, f"Player 2 Average Shot Type: {avg_player_2_shot_type}", ln=True)

    pdf.ln(10)

    # Provide performance improvement suggestions
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Performance Improvement Suggestions:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.ln(5)

    if avg_stats['player_1_last_shot_speed'] < 25:
        pdf.cell(0, 10, "Player 1: Consider working on increasing shot speed through strength and technique training.", ln=True)
    if avg_stats['player_1_last_player_speed'] < 15:
        pdf.cell(0, 10, "Player 1: Improve agility and movement speed through specific drills.", ln=True)

    if avg_stats['player_2_last_shot_speed'] < 25:
        pdf.cell(0, 10, "Player 2: Consider focusing on enhancing shot speed.", ln=True)
    if avg_stats['player_2_last_player_speed'] < 15:
        pdf.cell(0, 10, "Player 2: Work on footwork and overall speed.", ln=True)

    pdf.ln(10)

    # Generate and add graphs
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Statistical Graphs:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.ln(5)

    # Create and add graph for shot speeds
    plt.figure(figsize=(8, 6))
    plt.plot(player_stats.index + 1, player_stats['player_1_last_shot_speed'], label='Player 1 Shot Speed', marker='o')
    plt.plot(player_stats.index + 1, player_stats['player_2_last_shot_speed'], label='Player 2 Shot Speed', marker='o')
    plt.xlabel('Frame')
    plt.ylabel('Speed (km/h)')
    plt.title('Shot Speed Over Frames')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    graph_path = "shot_speed_graph.png"
    plt.savefig(graph_path)
    plt.close()

    if os.path.exists(graph_path):
        pdf.add_page()
        pdf.image(graph_path, x=10, y=pdf.get_y(), w=180)
    else:
        print("Error: Shot speed graph not saved correctly.")

    # Create and add graph for player speeds
    plt.figure(figsize=(8, 6))
    plt.plot(player_stats.index + 1, player_stats['player_1_last_player_speed'], label='Player 1 Speed', marker='o')
    plt.plot(player_stats.index + 1, player_stats['player_2_last_player_speed'], label='Player 2 Speed', marker='o')
    plt.xlabel('Frame')
    plt.ylabel('Speed (km/h)')
    plt.title('Player Speed Over Frames')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    graph_path = "player_speed_graph.png"
    plt.savefig(graph_path)
    plt.close()

    if os.path.exists(graph_path):
        pdf.add_page()
        pdf.image(graph_path, x=10, y=pdf.get_y(), w=180)
    else:
        print("Error: Player speed graph not saved correctly.")

    # Clean up temporary image files
    if os.path.exists("shot_speed_graph.png"):
        os.remove("shot_speed_graph.png")
    if os.path.exists("player_speed_graph.png"):
        os.remove("player_speed_graph.png")

    # Save PDF
    pdf_output_path = os.path.join(os.path.expanduser("~"), "Downloads", output_path)
    try:
        pdf.output(pdf_output_path)
    except Exception as e:
        print(f"Error saving PDF: {e}")
        return None

    return pdf_output_path

# Example usage
player_stats = pd.DataFrame({
    'player_1_last_shot_speed': [30, 40, 25],
    'player_2_last_shot_speed': [35, 45, 30],
    'player_1_last_player_speed': [12, 15, 10],
    'player_2_last_player_speed': [14, 17, 12],
    'player_1_average_shot_speed': [32, 38, 27],
    'player_2_average_shot_speed': [37, 42, 29],
    'player_1_average_player_speed': [13, 16, 11],
    'player_2_average_player_speed': [15, 18, 13]
})

output_pdf_path = generate_pdf_report(player_stats)
if output_pdf_path:
    print(f"PDF report generated at: {output_pdf_path}")
else:
    print("Failed to generate PDF report.")