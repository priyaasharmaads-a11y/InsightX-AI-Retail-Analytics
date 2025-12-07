from fpdf import FPDF

def sanitize_text(text: str) -> str:
    """
    Removes any characters that are not supported by latin-1.
    Also replaces symbols that commonly cause crashes.
    """
    return (
        text
        .replace("₹", "INR ")   # currency fix
        .replace("•", "- ")     # bullet fix
        .replace("–", "-")      # long dash
        .encode("latin-1", "ignore")
        .decode("latin-1")
    )

def generate_pdf_report(kpis, insights):
    """
    Returns PDF bytes with KPIs + insight bullets.
    Fully safe for latin-1 encoding.
    """
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, sanitize_text("InsightX Retail Sales Report"), ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "", 12)

    # ✅ Use sanitized INR values
    pdf.cell(0, 8, sanitize_text(f"Total Revenue: INR {kpis['total_revenue']:,}"), ln=True)
    pdf.cell(0, 8, sanitize_text(f"Total Orders: {kpis['total_transactions']}"), ln=True)
    pdf.cell(0, 8, sanitize_text(f"Average Order Value: INR {kpis['average_order_value']:.2f}"), ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, sanitize_text("Key Insights:"), ln=True)

    pdf.set_font("Arial", "", 12)
    pdf.ln(2)

    for line in insights:
        clean = sanitize_text(line.replace("**", ""))
        pdf.multi_cell(0, 6, f"- {clean}")

    # ✅ 100% safe export
    return pdf.output(dest="S").encode("latin-1", "ignore")

