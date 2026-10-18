import csv
import datetime
import sys
from pathlib import Path

CSV_PATH = Path('data/tax_deadlines.csv')
REQUIRED_COLUMNS = [
    'id',
    'tax_type',
    'title',
    'applicable_to',
    'deadline_rule',
    'source_url',
    'last_verified',
    'status',
]
ALLOWED_STATUSES = {
    'source_checked_rule_needs_review',
    'verified',
    'needs_review',
}


def fail(message):
    print(f'ERROR: {message}', file=sys.stderr)
    sys.exit(1)


def main():
    if not CSV_PATH.is_file():
        fail(f'CSV file not found: {CSV_PATH}')

    with CSV_PATH.open(encoding='utf-8-sig', newline='') as file:
        reader = csv.DictReader(file)

        if reader.fieldnames != REQUIRED_COLUMNS:
            fail(
                'Unexpected CSV columns. '
                f'Expected {REQUIRED_COLUMNS}; got {reader.fieldnames}'
            )

        seen_ids = set()
        count = 0

        for line_number, row in enumerate(reader, start=2):
            count += 1

            if None in row:
                fail(f'Wrong number of columns on line {line_number}')

            for column in REQUIRED_COLUMNS:
                if not row.get(column) or not row[column].strip():
                    fail(f'Missing {column} on line {line_number}')

            record_id = row['id'].strip()
            if record_id in seen_ids:
                fail(f'Duplicate id on line {line_number}: {record_id}')
            seen_ids.add(record_id)

            try:
                datetime.date.fromisoformat(row['last_verified'])
            except ValueError:
                fail(
                    f'Invalid last_verified date on line {line_number}; '
                    'use YYYY-MM-DD'
                )

            if row['status'] not in ALLOWED_STATUSES:
                fail(f'Unknown status on line {line_number}: {row["status"]}')

            if not row['source_url'].startswith('https://'):
                fail(f'source_url must use HTTPS on line {line_number}')

        if count == 0:
            fail('CSV contains no data records')

    print(f'OK: validated {count} tax deadline record(s).')


if __name__ == '__main__':
    main()
