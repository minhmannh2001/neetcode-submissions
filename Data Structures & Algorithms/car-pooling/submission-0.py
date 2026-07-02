class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # Sort theo điểm đón
        trips.sort(key=lambda trip: trip[1])

        ongoing_trips = []
        current_num_passengers = 0

        for trip in trips:
            num_passengers_in, start, end = trip

            new_ongoing_trips = []

            # Xử lý các chuyến đã kết thúc
            for ongoing_trip in ongoing_trips:
                passengers, _, ongoing_end = ongoing_trip

                if ongoing_end <= start:
                    current_num_passengers -= passengers
                else:
                    new_ongoing_trips.append(ongoing_trip)

            ongoing_trips = new_ongoing_trips

            # Đón khách mới
            current_num_passengers += num_passengers_in

            if current_num_passengers > capacity:
                return False

            # Thêm chuyến mới vào danh sách đang diễn ra
            ongoing_trips.append(trip)

        return True