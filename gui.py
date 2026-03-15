import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from main import analyze_folder


def browse_input_folder():
    folder = filedialog.askdirectory(title="Select Input Folder")
    if folder:
        input_folder_var.set(folder)


def browse_output_folder():
    folder = filedialog.askdirectory(title="Select Output Folder")
    if folder:
        output_folder_var.set(folder)


def run_analysis():
    input_folder = input_folder_var.get().strip()
    output_folder = output_folder_var.get().strip()
    case_name = case_name_var.get().strip()
    investigator_name = investigator_name_var.get().strip()

    if not input_folder:
        messagebox.showerror("Error", "Please select an input folder.")
        return

    if not output_folder:
        messagebox.showerror("Error", "Please select an output folder.")
        return

    if not case_name:
        messagebox.showerror("Error", "Please enter a case name.")
        return

    if not investigator_name:
        messagebox.showerror("Error", "Please enter an investigator name.")
        return

    try:
        status_label.config(text="Running analysis...")
        progress.start()
        root.update()

        results, report_path = analyze_folder(
            input_folder,
            output_folder,
            case_name,
            investigator_name
        )

        progress.stop()
        status_label.config(text="Analysis complete")

        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"Case Name: {case_name}\n")
        result_box.insert(tk.END, f"Investigator: {investigator_name}\n")
        result_box.insert(tk.END, f"Report Location:\n{report_path}\n\n")

        score = results["correlation_score"]
        conclusion = results["conclusion"]

        if score >= 8:
            color = "red"
        elif score >= 4:
            color = "orange"
        else:
            color = "green"

        result_box.insert(tk.END, f"Correlation Score: {score}\n\n")
        result_box.insert(tk.END, f"Conclusion: {conclusion}\n\n", color)

        result_box.tag_config("red", foreground="red", font=("Consolas", 12, "bold"))
        result_box.tag_config("orange", foreground="orange", font=("Consolas", 12, "bold"))
        result_box.tag_config("green", foreground="green", font=("Consolas", 12, "bold"))

        result_box.insert(tk.END, "Findings:\n\n")
        for finding in results["findings"]:
            result_box.insert(tk.END, f"• {finding}\n")

        messagebox.showinfo("Success", "Analysis completed successfully.")

    except Exception as e:
        progress.stop()
        status_label.config(text="Analysis failed")
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("TorArtifactAnalyzer")
root.geometry("780x620")
root.configure(bg="#E8ECEF")

input_folder_var = tk.StringVar(value="input")
output_folder_var = tk.StringVar(value="output")
case_name_var = tk.StringVar()
investigator_name_var = tk.StringVar()

title_label = tk.Label(
    root,
    text="TorArtifactAnalyzer",
    font=("Arial", 18, "bold"),
    bg="#E8ECEF"
)
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#E8ECEF")
frame.pack(padx=10, pady=10, fill="x")

tk.Label(frame, text="Case Name:", bg="#E8ECEF").grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(frame, textvariable=case_name_var, width=60).grid(row=0, column=1, padx=5, columnspan=2)

tk.Label(frame, text="Investigator Name:", bg="#E8ECEF").grid(row=1, column=0, sticky="w", pady=5)
tk.Entry(frame, textvariable=investigator_name_var, width=60).grid(row=1, column=1, padx=5, columnspan=2)

tk.Label(frame, text="Input Folder:", bg="#E8ECEF").grid(row=2, column=0, sticky="w", pady=5)
tk.Entry(frame, textvariable=input_folder_var, width=60).grid(row=2, column=1, padx=5)
tk.Button(frame, text="Browse", command=browse_input_folder).grid(row=2, column=2)

tk.Label(frame, text="Output Folder:", bg="#E8ECEF").grid(row=3, column=0, sticky="w", pady=5)
tk.Entry(frame, textvariable=output_folder_var, width=60).grid(row=3, column=1, padx=5)
tk.Button(frame, text="Browse", command=browse_output_folder).grid(row=3, column=2)

button_frame = tk.Frame(root, bg="#E8ECEF")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Run Analysis",
    command=run_analysis,
    width=20,
    height=2
).pack()

progress = ttk.Progressbar(root, mode="indeterminate", length=400)
progress.pack(pady=5)

status_label = tk.Label(root, text="Waiting for analysis...", bg="#E8ECEF")
status_label.pack()

result_box = tk.Text(
    root,
    height=20,
    width=92,
    bg="#F4F6F7",
    fg="#000000",
    font=("Consolas", 11)
)
result_box.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()