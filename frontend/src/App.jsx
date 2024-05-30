import './index.css';

import React, { useState } from 'react';

import GameCard from './components/GameCard';
import SearchForm from './components/SearchForm';
import SearchResult from './components/SearchResult';
import axios from 'axios';

const App = () => {
	const [query, setQuery] = useState('');
	const [searchResults, setSearchResults] = useState([]);
	const [selectedGame, setSelectedGame] = useState('');
	const [games, setGames] = useState([]);

	const handleChange = (e) => {
		setQuery(e.target.value);
	};

	const handleSearch = async (e) => {
		e.preventDefault();
		if (query) {
			try {
				const response = await axios.get(`http://localhost:5000/api/search`, {
					params: { query: query.trim() },
				});
				setSearchResults(response.data);
			} catch (error) {
				console.error('Error fetching games:', error);
			}
		} else {
			setSearchResults([]);
		}
	};

	const handleRecommend = async (title) => {
		setSelectedGame(title);
		try {
			const response = await axios.get(`http://localhost:5000/api/recommend`, {
				params: { title },
			});
			setGames(response.data);
		} catch (error) {
			console.error('Error fetching games:', error);
		}
	};

	return (
		<div className='p-6 relative'>
			<SearchForm
				query={query}
				handleChange={handleChange}
				handleSearch={handleSearch}
			/>
			<ul className='my-6 max-h-96 overflow-y-scroll'>
				{searchResults &&
					searchResults.map((title, index) => (
						<SearchResult
							key={index}
							title={title}
							handleRecommend={handleRecommend}
						/>
					))}
			</ul>
			<div className='grid grid-cols-2 gap-4'>
				{games &&
					games.map((game, index) => (
						<GameCard key={index} game={game} selectedGame={selectedGame} />
					))}
			</div>
		</div>
	);
};

export default App;
