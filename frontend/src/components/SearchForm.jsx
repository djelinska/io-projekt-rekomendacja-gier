import { PiMagnifyingGlassBold } from 'react-icons/pi';

const SearchForm = ({ query, handleChange, handleSearch }) => {
	return (
		<form onSubmit={handleSearch} className='max-w-lg mx-auto relative'>
			<div className='absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none'>
				<PiMagnifyingGlassBold className='w-4 h-4 text-gray-400' />
			</div>
			<input
				type='search'
				className='block w-full p-4 ps-10 font-sans border border-gray-600 rounded-lg bg-gray-700 focus:outline-none focus:ring-blue-500 focus:border-blue-500 placeholder-gray-400'
				placeholder='Search for games...'
				value={query}
				onChange={handleChange}
			/>
			<button
				type='submit'
				className='font-medium rounded-md text-sm px-4 py-2 absolute end-2.5 bottom-2.5 bg-blue-600 hover:bg-blue-700 focus:ring-1 focus:outline-none focus:ring-blue-800'
			>
				Search
			</button>
		</form>
	);
};

export default SearchForm;
