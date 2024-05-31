const SearchResult = ({ title, handleRecommend }) => {
	return (
		<li className='mx-4 py-2 flex justify-between items-center border-b border-b-gray-700'>
			<p>{title}</p>
			<button
				onClick={() => handleRecommend(title)}
				className='bg-gray-800 hover:bg-gray-700 focus:outline-none focus:ring-1 focus:ring-gray-700 font-medium rounded-md text-sm px-4 py-2 border-gray-700'
			>
				Show Similar Games
			</button>
		</li>
	);
};

export default SearchResult;
