import './globals.css';

export const metadata = {
  title: 'Modern Todo Application',
  description: 'A beautiful and functional todo application',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-[color:rgb(var(--background-rgb))] text-[color:rgb(var(--text-primary-rgb))]">
        <div className="container mx-auto px-4 max-w-4xl">
          <main className="animate-fade-in">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}