import classNames from "classnames";
import "./App.css";

function Table(props) {
  console.log(props);
  return (
    <div className="w-full mt-16 mx-auto">
      <div className="flex flex-col">
        <div className="overflow-x-auto shadow-md sm:rounded-lg">
          <div className="inline-block min-w-full align-middle">
            <div className="overflow-hidden ">
              <table className="min-w-full divide-y divide-gray-200 table-fixed dark:divide-gray-700">
                <thead className="bg-gray-100 dark:bg-gray-700">
                  <tr>
                    <th
                      scope="col"
                      className="py-3 px-6 text-xs font-medium tracking-wider text-left text-gray-700 uppercase dark:text-gray-400"
                    >
                      Category
                    </th>
                    <th
                      scope="col"
                      className="py-3 px-6 text-xs font-medium tracking-wider text-left text-gray-700 uppercase dark:text-gray-400"
                    >
                      Is Valid?
                    </th>
                    <th scope="col" className="p-4">
                      <span className="sr-only">Edit</span>
                    </th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200 dark:bg-gray-800 dark:divide-gray-700">
                  {/* loop through the rows hash, to build the output table */}
                  {Object.entries(props.rows).map(([key, value]) => {
                    return (
                      <tr className="hover:bg-gray-100 dark:hover:bg-gray-700">
                        <td className="py-4 px-6 text-sm font-medium text-gray-900 w-2/3 whitespace-nowrap dark:text-white">
                          {key}
                        </td>
                        <td
                          className={classNames({
                            "py-4 px-6 text-sm font-medium w-1/3 whitespace-nowrap font-extrabold": true,
                            "text-red-800": value === "0",
                            "text-green-800": value !== "0",
                          })}
                        >
                          {value === "0" ? "No" : "Yes"}
                        </td>
                        <td></td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

      <p className="mt-5">
        This table component is part of a larger, open-source library of
        Tailwind CSS components. Learn more by going to the official{" "}
        <a
          className="text-blue-600 hover:underline"
          href="https://flowbite.com/docs/getting-started/introduction/"
          target="_blank"
        >
          Flowbite Documentation
        </a>
        .
      </p>
    </div>
  );
}

export default Table;
