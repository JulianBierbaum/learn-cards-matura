
export default function Home() {
  return (
    <main className="container mx-auto p-6">
      <h1 className="text-2xl font-bold mb-6">Overview</h1>
      <div className="mb-8 overflow-hidden rounded-lg border border-gray-200 bg-white shadow-sm">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">Kategorie</th>
              <th className="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">Information</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200 bg-white">
            <tr>
              <td className="whitespace-nowrap px-6 py-4 font-medium text-gray-900">Name</td>
              <td className="whitespace-nowrap px-6 py-4 text-gray-600">John Doe</td>
            </tr>
            <tr>
              <td className="whitespace-nowrap px-6 py-4 font-medium text-gray-900">Fach</td>
              <td className="whitespace-nowrap px-6 py-4 text-gray-600">Softwareentwicklung</td>
            </tr>
            <tr>
              <td className="whitespace-nowrap px-6 py-4 font-medium text-gray-900">Datum</td>
              <td className="whitespace-nowrap px-6 py-4 text-gray-600">08.05.2026</td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  );
}