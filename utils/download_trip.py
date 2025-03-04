from fpdf import FPDF
import streamlit as st
import os

class PDFDownloader:
    def __init__(self, user_details, ai_response):
        self.user_details = user_details
        self.ai_response = ai_response

    def generate_trip_pdf(self):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, "Your AI-Powered Trip Plan", ln=True, align="C")
        pdf.ln(10)

        pdf.multi_cell(0, 10, f"Your {self.user_details['duration']}-day trip to {self.user_details['destination']} is ready!")
        pdf.ln(5)
        pdf.multi_cell(0, 8, f"Duration: {self.user_details['duration']} days\nBudget: Rs. {self.user_details['budget']}")
        pdf.ln(10)

        pdf.multi_cell(0, 8, self.ai_response)
        pdf.ln(5)

        pdf_path = "Trip_Plan.pdf"  
        pdf.output(pdf_path, 'F')

        return pdf_path

    def download_pdf_button(self):
        pdf_path = self.generate_trip_pdf()

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="📥 Download Trip PDF",
                data=pdf_file,
                file_name="Trip_Plan.pdf",
                mime="application/pdf"
            )
        os.remove(pdf_path)
