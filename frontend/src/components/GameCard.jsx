import { PiGameControllerFill } from 'react-icons/pi';

const GameCard = ({ game, selectedGame }) => {
	return (
		<div className='flex items-center border rounded-md border-gray-700 bg-gray-800'>
			<div className='flex justify-center items-center'>
				<PiGameControllerFill className='text-3xl m-8' />
			</div>
			<div className='flex flex-col h-full p-4 gap-2'>
				{game.title == selectedGame && (
					<span className='uppercase font-semibold text-sm text-blue-400'>
						Selected Game
					</span>
				)}
				<h2 className='text-2xl font-semibold tracking-tight'>{game.title}</h2>
				<div className='flex items-center gap-2 flex-wrap'>
					{game.popular_tags.slice(0, 3).map((tag, index) => (
						<div
							key={index}
							className='p-2 w-fit rounded-md tracking-wider font-medium text-xs uppercase bg-gray-900'
						>
							{tag}
						</div>
					))}
				</div>
				<p className='text-gray-400'>{game.description}</p>
			</div>
		</div>
	);
};

export default GameCard;
